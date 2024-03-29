from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.password_validation import validate_password
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.mail import get_connection, EmailMessage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from ecommerce.apps.orders.models import Order
from ecommerce.apps.orders.views import user_orders
from ecommerce.apps.catalogue.models import Product
from .forms import RegistrationForm, UserEditForm, UserAddressForm
from .models import Customer, Address
from .token import account_activation_token


@login_required
def dashboard(request):
    orders = user_orders(request)
    return render(request, "account/dashboard/dashboard.html", {"orders": orders})


def account_register(request):
    if request.user.is_authenticated:
        return redirect('account:dashboard')
    if request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.email = register_form.cleaned_data["email"]
            user.name = register_form.cleaned_data["name"]
            user.password = register_form.cleaned_data["password"]
            try:
                validate_password(user.password)
            except ValidationError as e:
                error_message = e.messages[0]
                register_form = RegistrationForm()
                return render(request, "account/registration/register.html", {"error_message": error_message,
                                                                              "form": register_form})
            user.set_password(user.password)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = "Activate your Account"
            message = render_to_string("account/registration/account_activation_email.html", {
                "name": user.name,
                "dashboard": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": account_activation_token.make_token(user),
            })
            with get_connection(
                    host=settings.EMAIL_HOST,
                    port=settings.EMAIL_PORT,
                    username=settings.EMAIL_HOST_USER,
                    password=settings.EMAIL_HOST_PASSWORD,
                    use_tls=settings.EMAIL_USE_TLS
            ) as connection:
                subject = subject
                email_from = settings.EMAIL_HOST_USER
                recipient = [user.email]
                message = message
                EmailMessage(subject, message, email_from, recipient, connection=connection).send()
            # user.email_user(subject=subject, message=message)
            # print(message)
            return render(request, "account/registration/register_email_confirm.html", {"form": register_form})
        else:
            HttpResponse("Error handler content", status=400)
    else:
        register_form = RegistrationForm()
    return render(request, "account/registration/register.html", {"form": register_form})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Customer.objects.get(pk=uid)
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect("account:dashboard")
        else:
            return render(request, "account/registration/invalid_activation.html")
    except(TypeError, ValueError, OverflowError):
        user = None


@login_required
def edit_details(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request, "account/dashboard/edit_details.html", {"user_form": user_form})


@login_required
def delete_user(request):
    user = Customer.objects.get(name=request.user)
    user.is_active = False
    user.save()
    logout(request)
    return redirect("account:delete_confirmation")


# Addresses Section

@login_required
def view_address(request):
    addresses = Address.objects.filter(customer=request.user)
    return render(request, "account/dashboard/addresses.html", {"addresses": addresses})


@login_required
def add_address(request):
    if request.method == "POST":
        address_form = UserAddressForm(data=request.POST)
        if address_form.is_valid():
            address_form = address_form.save(commit=False)
            address_form.customer = request.user
            address_form.save()
            return HttpResponseRedirect(reverse("account:addresses"))
        else:
            return HttpResponse("Error handler content", status=400)
    else:
        address_form = UserAddressForm()
    return render(request, "account/dashboard/edit_addresses.html", {"form": address_form})


@login_required
def edit_address(request, id):
    if request.method == "POST":
        address = Address.objects.get(pk=id, customer=request.user)
        address_form = UserAddressForm(instance=address, data=request.POST)
        if address_form.is_valid():
            address_form.save()
            return HttpResponseRedirect(reverse("account:addresses"))
    else:
        address = Address.objects.get(pk=id, customer=request.user)
        address_form = UserAddressForm(instance=address)
    return render(request, "account/dashboard/edit_addresses.html", {"form": address_form})


@login_required
def delete_address(request, id):
    address = Address.objects.filter(pk=id, customer=request.user).delete()
    return redirect("account:addresses")


@login_required
def set_default(request, id):
    Address.objects.filter(customer=request.user, default=True).update(default=False)
    Address.objects.filter(pk=id, customer=request.user).update(default=True)
    previous_url = request.META["HTTP_REFERER"]
    if "delivery_address" in previous_url:
        return redirect("checkout:delivery_address")
    return redirect("account:addresses")


# Orders Section

@login_required
def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return render(request, "account/dashboard/user_orders.html", {"orders": orders})


# Wishlist Section

@login_required
def wishlist(request):
    products = Product.objects.filter(user_wishlist=request.user)
    return render(request, "account/dashboard/user_wishlist.html", {"wishlist": products})


@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    if product.user_wishlist.filter(id=request.user.id).exists():
        product.user_wishlist.remove(request.user)
        messages.success(request, f"Removed {product.title} from your Wish List.")
    else:
        product.user_wishlist.add(request.user)
        messages.success(request, f"Added {product.title} to your Wish List.")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm

from .models import Customer


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control mb-3",
            "placeholder": "Email",
            "id": "login-username",
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "placeholder": "Password",
            "id": "login-password",
        }
    ))


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label="Enter Username ", min_length=4, max_length=30, help_text="Required")
    email = forms.EmailField(label="Email ", max_length=50, help_text="Required", error_messages={
        "Required": "You have to add your email address."
    })
    password = forms.CharField(label="Password ", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password ", widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('user_name', 'email',)

    def clean_username(self):
        user_name = self.cleaned_data["user_name"].lower()
        r = Customer.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError("Username already exists.")
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords do not match.")
        return cd["password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists in the database. Try to log in instead.")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_name"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Username"})
        self.fields["email"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Email", "name": "email", "id": "id_email"})
        self.fields["password"].widget.attrs.update(
            {"class": "form-control mb-3", "placeholder": "Password"})
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Repeat Password"})


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(
        label="Account email (can not be changed)", max_length=200, widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Email",
                "id": "form-email",
                "readonly": "readonly"
            }
        ))
    user_name = forms.CharField(
        label="Username (can not be changed)", min_length=4, max_length=50, widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Username",
                "id": "form-username",
                "readonly": "readonly"
            }
        ))
    first_name = forms.CharField(
        label="First name", min_length=2, max_length=50, widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Firstname",
                "id": "form-firstname"
            }
        ))
    surname = forms.CharField(
        label="Surname", min_length=2, max_length=50, widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Surname",
                "id": "form-surname"
            }
        ))
    about = forms.CharField(
        label="About", min_length=4, max_length=500, widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "About",
                "id": "form-about"
            }
        ))
    country = forms.CharField(
        label="Country", min_length=2, max_length=50, widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "country",
                "id": "form-country"
            }
        ))
    phone_number = forms.CharField(
        label="Phone Number", min_length=4, max_length=15, widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "phone-number",
                "id": "form-phone-number"
            }
        ))
    postcode = forms.CharField(
        label="Postcode", min_length=4, max_length=10, widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Postcode",
                "id": "form-postcode"
            }
        ))
    address_1 = forms.CharField(
        label="Address 1", min_length=4, max_length=100, widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Address-1",
                "id": "form-address-1"
            }
        ))
    address_2 = forms.CharField(
        label="Address 2", min_length=0, max_length=100, widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Address-2",
                "id": "form-address-2"
            }
        ))
    city = forms.CharField(
        label="City", min_length=2, max_length=50, widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "City",
                "id": "form-city"
            }
        ))

    class Meta:
        model = Customer
        fields = ("email", "user_name", "first_name", "surname", "about", "country", "phone_number", "postcode",
                  "address_1", "address_2", "city",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_name"].required = True
        self.fields["email"].required = True


class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={
            "class": "form-control mb-3",
            "placeholder": "Email",
            "id": "form-email",
        }
    ))

    def clean_email(self):
        email = self.cleaned_data["email"]
        u = Customer.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                "We could not find this account, sorry."
            )
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password", widget=forms.PasswordInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "New Password",
                "id": "form-newpassword1",
            }
        ))

    new_password2 = forms.CharField(
        label="Repeat password", widget=forms.PasswordInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "New Password",
                "id": "form-newpassword2",
            }
        ))

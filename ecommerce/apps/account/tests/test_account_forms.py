import pytest
from ecommerce.apps.account.forms import RegistrationForm, UserAddressForm


@pytest.mark.parametrize(
    "full_name, phone, address_line_1, address_line_2, postcode, town_city, validity",
    [
        ("John Doe", "111222333", "address1", "address2", "11-222", "City", True),
        ("", "111222333", "address1", "address2", "11-222", "City", False),
    ]
)
def test_customer_address(full_name, phone, address_line_1, address_line_2, postcode, town_city, validity):
    form = UserAddressForm(
        data={
            "full_name": full_name,
            "phone": phone,
            "address_line_1": address_line_1,
            "address_line_2": address_line_2,
            "postcode": postcode,
            "town_city": town_city,
        }
    )
    assert form.is_valid() is validity


def test_customer_create_address(client, customer):
    user = customer
    client.force_login(user)
    response = client.post("/account/add_address/", data={
        "full_name": "John Doe",
        "phone": "111222333",
        "address_line_1": "address1",
        "address_line_2": "address2",
        "postcode": "12345",
        "town_city": "City",
    })
    assert response.status_code == 302


@pytest.mark.parametrize(
    "name, email, password, password2, validity",
    [
        ("user1", "a@a.com", "test123", "test123", True),
        ("user1", "a@a.com", "test123", "", False),
        # ("user1", "a@a.com", "", "test123", False),
        ("user1", "a@a.com", "test", "123", False),
        ("user1", "a.com", "test123", "test123", False),
    ]
)
@pytest.mark.django_db
def test_create_account(name, email, password, password2, validity):
    form = RegistrationForm(
        data={
            "name": name,
            "email": email,
            "password": password,
            "password2": password2,
        }
    )
    assert form.is_valid() is validity


@pytest.mark.parametrize(
    "name, email, password, password2, validity",
    [
        ("user1", "a@a.com", "test123", "test123", 200),
        # ("user1", "a@a.com", "test123", "test", 400),
        # ("user1", "", "test123", "test123", 400),
    ]
)
@pytest.mark.django_db
def test_create_account_view(client, name, email, password, password2, validity):
    response = client.post(
        "/account/register/",
        data={
            "name": name,
            "email": email,
            "password": password,
            "password2": password2,
        },
    )
    assert response.status_code is validity


def test_account_register_redirect(client, customer):
    user = customer
    client.force_login(user)
    response = client.get("/account/register/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_account_register_render(client):
    response = client.get("/account/register/")
    assert response.status_code == 200

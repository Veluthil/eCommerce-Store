import pytest
from ecommerce.apps.account.forms import RegistrationForm, UserAddressForm


@pytest.mark.parametrize(
    "full_name, phone, address_line_1, address_line_2, postcode, town_city, validity",
    [
        ("John Doe", "111222333", "address1", "address2", "11-222", "City", True),
        # ("", "111222333", "address1", "address2", "11-222", "City", False),
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

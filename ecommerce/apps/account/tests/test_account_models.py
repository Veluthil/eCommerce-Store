import pytest


def test_customer_str(customer):
    assert customer.__str__() == "user1"


def test_admin_str(admin_user):
    assert admin_user.__str__() == "admin_user"


def test_customer_email_no_input(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="")
    assert str(e.value) == "Customer Account: you must provide a valid email address."


def test_customer_email_incorrect(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="incorrect.email")
    assert str(e.value) == "You must provide a valid email address."


def test_admin_user_email_no_input(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="", is_superuser=True, is_staff=True)
    assert str(e.value) == "Superuser Account: you must provide a valid email address."


def test_admin_user_email_incorrect(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="incorrect.email", is_superuser=True, is_staff=True)
    assert str(e.value) == "You must provide a valid email address."


def test_admin_user_email_not_staff(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="", is_superuser=True, is_staff=False)
    assert str(e.value) == "Superuser must be assigned to is_staff=True."


def test_admin_user_email_not_superuser(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="incorrect.email", is_superuser=False, is_staff=True)
    assert str(e.value) == "Superuser must be assigned to is_superuser=True."


def test_address_str(address):
    full_name = address.full_name
    assert address.__str__() == f"{full_name}'s Address"

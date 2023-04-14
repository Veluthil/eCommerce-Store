from django.urls import reverse


def test_root_url(db, client):
    url = reverse("catalogue:catalogue_home")
    response = client.get(url)
    assert response.status_code == 200

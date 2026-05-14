import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.api
def test_products_endpoint_returns_catalog():
    response = client.get("/products")
    products = response.json()

    assert response.status_code == 200
    assert isinstance(products, list)
    assert products[0]["id"] == 1
    assert "price" in products[0]


@pytest.mark.api
def test_product_detail_endpoint_returns_product():
    response = client.get("/products/1")
    product = response.json()

    assert response.status_code == 200
    assert product["id"] == 1
    assert product["name"] == "Café DevOps"


@pytest.mark.api
def test_product_detail_endpoint_returns_404_when_missing():
    response = client.get("/products/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"

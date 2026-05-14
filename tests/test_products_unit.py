import pytest

from app.products import get_product, list_products


@pytest.mark.unit
def test_list_products_returns_initial_catalog():
    products = list_products()

    assert len(products) >= 3
    assert products[0]["name"] == "Café DevOps"


@pytest.mark.unit
def test_get_product_returns_existing_product():
    product = get_product(1)

    assert product is not None
    assert product["id"] == 1
    assert "price" in product


@pytest.mark.unit
def test_get_product_returns_none_when_missing():
    product = get_product(999)

    assert product is None

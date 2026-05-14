"""Catálogo inicial de productos para Tienda Ágora."""

from typing import Any

PRODUCTS: list[dict[str, Any]] = [
    {
        "id": 1,
        "name": "Café DevOps",
        "price": 12.50,
        "stock": 25,
    },
    {
        "id": 2,
        "name": "Teclado CI/CD",
        "price": 45.00,
        "stock": 10,
    },
    {
        "id": 3,
        "name": "Cuaderno Pipeline",
        "price": 7.75,
        "stock": 40,
    },
]


def list_products() -> list[dict[str, Any]]:
    """Devuelve todos los productos disponibles."""
    return PRODUCTS


def get_product(product_id: int) -> dict[str, Any] | None:
    """Devuelve un producto por identificador."""
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None

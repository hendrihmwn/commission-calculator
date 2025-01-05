from schemas.schema import ProductSalesPoint
PRODUCT_SALES_POINT = [
    {
        "item": "red",
        "product_point": 5000,
        "sales_point": 1
    },
    {
        "item": "blue",
        "product_point": 10000,
        "sales_point": 2
    },
    {
        "item": "yellow",
        "product_point": 25000,
        "sales_point": 3
    }
]

def get_by_item(item: str) -> ProductSalesPoint:
    product = next((entry for entry in PRODUCT_SALES_POINT if entry["item"] == item), None)
    if product:
        return ProductSalesPoint(**product)
    else:
        return None
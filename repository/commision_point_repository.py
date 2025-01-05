from schemas.schema import CommissionPoint, InputFindCommissionPoint

COMMISSION_POINT = [
    {
        "type": "SP",
        "min_sales_point": 1,
        "max_sales_point": 3,
        "commission_point": 75,
    },
    {
        "type": "SP",
        "min_sales_point": 4,
        "max_sales_point": 7,
        "commission_point": 100,
    },
    {
        "type": "SP",
        "min_sales_point": 8,
        "max_sales_point": 10,
        "commission_point": 125,
    },
    {
        "type": "SP",
        "min_sales_point": 11,
        "max_sales_point": 15,
        "commission_point": 150,
    },
    {
        "type": "SP",
        "min_sales_point": 15,
        "max_sales_point": 99999999,
        "commission_point": 200,
    },
    {
        "type": "SM",
        "min_sales_point": 1,
        "max_sales_point": 5,
        "commission_point": 75,
    },
    {
        "type": "SM",
        "min_sales_point": 6,
        "max_sales_point": 9,
        "commission_point": 100,
    },
    {
        "type": "SM",
        "min_sales_point": 10,
        "max_sales_point": 14,
        "commission_point": 125,
    },
    {
        "type": "SM",
        "min_sales_point": 15,
        "max_sales_point": 19,
        "commission_point": 150,
    },
    {
        "type": "SM",
        "min_sales_point": 20,
        "max_sales_point": 99999999,
        "commission_point": 200,
    },
    {
        "type": "GM",
        "min_sales_point": 1,
        "max_sales_point": 20,
        "commission_point": 75,
    },
    {
        "type": "GM",
        "min_sales_point": 21,
        "max_sales_point": 49,
        "commission_point": 100,
    },
    {
        "type": "GM",
        "min_sales_point": 50,
        "max_sales_point": 74,
        "commission_point": 125,
    },
    {
        "type": "GM",
        "min_sales_point": 75,
        "max_sales_point": 99,
        "commission_point": 150,
    },
    {
        "type": "GM",
        "min_sales_point": 100,
        "max_sales_point": 99999999,
        "commission_point": 200,
    }
]

def get_commission_point(data: InputFindCommissionPoint) -> CommissionPoint:
    product = next((entry for entry in COMMISSION_POINT 
                    if entry["type"] == data.type and 
                    entry["min_sales_point"] <= data.sales_point and 
                    entry["max_sales_point"] >= data.sales_point), None)
    if product:
        return CommissionPoint(**product)
    else:
        return None
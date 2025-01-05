from pydantic import BaseModel, Field
from typing import Optional

class ProductSalesPoint(BaseModel):
    item: str
    product_point: int
    sales_point: int

class CommissionPoint(BaseModel):
    type: str
    min_sales_point: int
    max_sales_point: int
    commission_point: int

class PerformanceIncentive(BaseModel):
    type: str
    min_sales_point: int
    max_sales_point: int
    min_active_person: int
    max_active_person: int
    incentive: int

class InputFindCommissionPoint(BaseModel):
    type: str
    sales_point: int

class InputFindPerformanceIncentive(BaseModel):
    type: str
    sales_point: int
    active_person: int

class SalesData(BaseModel):
    so: str
    sp: str
    sm: str
    gm: str
    item: str

class Commission(BaseModel):
    item: str
    total_item: int
    total_sales_point: int
    commission_point: int = 0
    basic_commission: float = 0

class PersonResult(BaseModel):
    name: str
    total_sales: int = 0
    commissions: dict[str, Commission]
    total_sales_point: int
    sm: str = ""
    gm: str = ""
    list_active_sp: set[str] = Field(default_factory=set)
    list_active_sm: set[str] = Field(default_factory=set)
    performance_incentive: int = 0

class ResponseCalculation(BaseModel):
    name: str
    commissions: Commission
    total_sales_point: int
    total_active: int
    performance_incentive: int
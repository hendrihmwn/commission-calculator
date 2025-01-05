from schemas.schema import SalesData, Commission, PersonResult, InputFindCommissionPoint, InputFindPerformanceIncentive
from typing import Dict

import repository.product_sales_point_repository as product_sales_point_repository
import repository.commision_point_repository as commision_point_repository
import repository.performance_incentive_repository as performance_incentive_repository

def calculate(data: list[SalesData]) -> Dict[str, Dict[str, PersonResult]]:
    dict_result_sp: Dict[str, PersonResult] = {}
    dict_result_sm: Dict[str, PersonResult] = {}
    dict_result_gm: Dict[str, PersonResult] = {}

    # divide data into per person
    # calculate sales point
    for v in data:
        key_sp = v.sp
        result = dict_result_sp.get(key_sp, None)
        assign_sales_point("SP", key_sp, v, result, dict_result_sp)

        key_sm = v.sm
        result = dict_result_sm.get(key_sm, None)
        assign_sales_point("SM", key_sm, v, result, dict_result_sm)

        key_gm = v.gm
        result = dict_result_gm.get(key_gm, None)
        assign_sales_point("GM", key_gm, v, result, dict_result_gm)

    
    # Calculate Basic Incentive & Performance Incentive
    # SP
    for v in dict_result_sp.values():
        incentive_calculation("SP", v)

    # SM
    for v in dict_result_sm.values():
        incentive_calculation("SM", v)

    # GM
    for v in dict_result_gm.values():
        incentive_calculation("GM", v)

    result = dict()
    result["SP"] = dict_result_sp
    result["SM"] = dict_result_sm
    result["GM"] = dict_result_gm    
    return result

def assign_sales_point(role: str, key: str, data: SalesData, result: PersonResult, dict_result: Dict[str, PersonResult]):
    product_sales = product_sales_point_repository.get_by_item(data.item)
    if result is not None:
        result.total_sales += 1
        result.total_sales_point += product_sales.sales_point
        # calculate total sales point per item
        commission = result.commissions.get(data.item, None)
        if commission is not None:
            commission.total_sales_point += product_sales.sales_point
            commission.total_item += 1
        else:
            result.commissions[data.item] = Commission(
                item=data.item,
                total_item=1,
                total_sales_point=product_sales.sales_point
            )
        
        if role == "SM":
            result.list_active_sp.add(data.sp)
        
        if role == "GM":
            result.list_active_sm.add(data.sm)
    else:
        # initiate sales point per item
        commissions: Dict[str, Commission] = {}
        commissions[data.item] = Commission(
            item=data.item, 
            total_item=1,
            total_sales_point=product_sales.sales_point)

        # initiate incentive data per person
        dict_result[key] = PersonResult(
            name=key,
            commissions=commissions,
            total_sales=1,
            total_sales_point=product_sales.sales_point,
        )

        if role == "SP":
            dict_result[key].sm = data.sm
            dict_result[key].gm = data.gm

        if role == "SM":
            list_active = dict_result[key].list_active_sp
            list_active.add(data.sp)
            dict_result[key].gm = data.gm
        
        if role == "GM":
            list_active = dict_result[key].list_active_sm
            list_active.add(data.sm)

def incentive_calculation(role: str, data: PersonResult):
    active_person = 0
    if role == "SP":
        active_person = 0

    if role == "SM":
        active_person = len(data.list_active_sp)
        
    if role == "GM":
        active_person = len(data.list_active_sm)

    # calculate basic commission per items
    for v in data.commissions.values():
        product_sales = product_sales_point_repository.get_by_item(v.item)
        commission_point = commision_point_repository.get_commission_point(InputFindCommissionPoint(
                type=role, sales_point=v.total_sales_point
            ))
        if commission_point is not None:
            v.commission_point = commission_point.commission_point
            v.basic_commission = product_sales.product_point * v.commission_point / 100
    
    # calculate performance incentive
    input_data = InputFindPerformanceIncentive(
        type=role, sales_point=data.total_sales_point, active_person=active_person
    )

    performance_incentive = performance_incentive_repository.get_by_item(input_data)
    if performance_incentive is not None:
        data.performance_incentive = performance_incentive.incentive
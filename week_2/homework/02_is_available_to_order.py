# 이분정렬은 sort 되어 있어야 사용 가능!
# Q. are the orders in the menu? A. T/F

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

def is_available_to_order(menus, orders):
    menus.sort()
    orders.sort()

    # orders에 하나라도 없으면 return False
    for n in range(len(orders)):
        cur_min_index = 0
        cur_max_index = len(menus) - 1
        cur_target_index = (cur_max_index + cur_max_index) // 2
        order_possibility = False

        while cur_min_index <= cur_max_index:
            if menus[cur_target_index] == orders[n]:
                order_possibility = True
                break
            elif menus[cur_target_index] < orders[n]:
                cur_min_index = cur_target_index + 1
            else:
                cur_max_index = cur_target_index - 1
            cur_target_index = (cur_min_index + cur_max_index) // 2

        if order_possibility is not True:
            return False

    return order_possibility


result = is_available_to_order(shop_menus, shop_orders)
print(result)
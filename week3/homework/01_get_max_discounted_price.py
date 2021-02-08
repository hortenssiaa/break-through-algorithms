# 단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다.
# 가장 큰 가격 - 할인율 높은 쿠폰
# ...
# Q. 이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?

shop_prices = [30000, 2000, 1500000]  # 가격
user_coupons = [20, 40]  # 쿠폰 (%)


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)  # [1500000, 30000, 2000]
    coupons.sort(reverse=True)  # [40, 20]
    total_price = 0

    for i in range(len(coupons)):
        prices[i] = prices[i] * (100 - coupons[i]) / 100

    for price in prices:
        total_price += price

    return int(total_price)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
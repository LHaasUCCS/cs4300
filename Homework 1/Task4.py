def calculate_discount(price, discount):
    price_off = price * discount
    return price - price_off

def test_calculate_discount():
    assert calculate_discount(300, 1) == 0
    assert calculate_discount(47, .15) == 39.95
    assert calculate_discount(20, -.25) == 25

print(f"the new price is: {calculate_discount(34.50, 0.20):.2f}")
print(f"the new price is: {calculate_discount(12, 0.45):.2f}")
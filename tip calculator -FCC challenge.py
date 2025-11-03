

def calculate_tips(meal_price, custom_tip):
    ct = int(custom_tip[:len(custom_tip)-1])/100
    return [f"${(float(meal_price[1:]) * per):.2f}" for per in [0.15, 0.2, ct]]



print(calculate_tips("$10.00", "25%"))
print(calculate_tips("$89.67", "26%"))



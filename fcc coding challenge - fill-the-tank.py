
def cost_to_fill(tank_size, fuel_level, price_per_gallon):

    return f"${((tank_size - fuel_level)*price_per_gallon):.2f}"



print(cost_to_fill(20, 0, 4.00))
print(cost_to_fill(18, 9, 3.25))
print(cost_to_fill(15, 10, 3.50))


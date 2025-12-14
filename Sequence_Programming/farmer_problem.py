acres = 16

tomato_yield = (0.3 * acres * 10 + 0.7 * acres * 12) * 1000 * 7
potato_yield = acres * 10 * 1000 * 20
cabbage_yield = acres * 14 * 1000 * 24
sunflower_yield = acres * 0.7 * 1000 * 200
sugarcane_yield = acres * 45 * 4000

total_sales = tomato_yield + potato_yield + cabbage_yield + sunflower_yield + sugarcane_yield
chemical_free_sales = tomato_yield + potato_yield + cabbage_yield + sunflower_yield

print("Overall Sales:", total_sales)
print("Chemical-free Sales after 11 months:", chemical_free_sales)

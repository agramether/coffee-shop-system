#sept 16, 2026

menu1 = {"E1 - Americano (Espresso-Based)": "Php 120",
        "E2 - Latte (Espresso-Based)": "Php 125",
        "E3 - Spanish Latte (Espresso-Based)": "Php 130",
        "N1 - Chocolate (Non-Coffee)": "Php 115",
        "N2- Hojicha (Non-Coffee)": "Php 135",
        "F1 - Mocha Frappe (Frappe/Blended)": "Php 150",
        "F2 - Caramel Frappe (Frappe/Blended)": "Php 155"
    }

drink_code = ["E1", "E2", "E3", "N1", "N2", "F1", "F2"]
drinks = ["Americano", "Latte", "Spanish Latte", "Chocolate", "Hojicha", "Mocha Frappe", "Caramel Frappe"]
price = [120, 125, 130, 115, 135, 150, 155]

menu = {}

for i in range(len(drink_code) and len(drinks) and len(price)):
    print(f"{drink_code[i]} - {drinks[i]}: ${price[i]}")
    

    


#oct 4
#to reference: searched for how to have uniform amount of spaces between each statement
#https://www.w3schools.com/python/python_string_formatting.asp


menu = {
    "E": {
        "1": {"name": "Americano", "price": 120},
        "2": {"name": "Latte", "price": 125},
        "3": {"name": "Spanish Latte", "price": 130}
    },
    "N": {
        "1": {"name": "Chocolate", "price": 115},
        "2": {"name": "Hojicha", "price": 135}
    },
    "F": {
        "1": {"name": "Mocha Frappe", "price": 150},
        "2": {"name": "Caramel Frappe", "price": 155}
    }
}

sizes = {"S": {"size": "Small", "price": 0},
         "M": {"size": "Medium", "price": 25},
         "L": {"size": "Large", "price": 50}
         }

print("DRINK CATALOG")
print()
print("ESPRESSO-BASED")
for i in menu["E"]:
    print(f" E{i:<2}   ${menu['E'][i]['price']:<3}   {menu['E'][i]['name']} ")
print("NON-COFFEE")
for i in menu["N"]:
    print(f" N{i:<2}   ${menu['N'][i]['price']:<3}   {menu['N'][i]['name']} ")
print("FRAPPE/BLENDED")
for i in menu["F"]:
    print(f" F{i:<2}   ${menu['F'][i]['price']:<3}   {menu['F'][i]['name']} ")
print()
print("SIZES")
for i in sizes:
    print(f" {i:<2}   +${sizes[i]['price']:<3}   {sizes[i]['size']} ")


#########################################
print()
print("***********")
print(menu.keys())
print(menu["E"]["1"]["name"]) #name of the first value in key E
print(menu["E"]["1"]["price"]) #price of the first value in key E
print(menu["E"]["2"]["name"]) #name of the second value in key E
#WORK IT BACKWARDS



#ver1 of coffee shop ordering system
#sept 15, 2026
#ver2 of coffee shop ordering system
#oct 4, 2026 (moved to vscode)


def main_menu (): #SYSTEM: then function for each so that when user inputs 1, it calls the function for main menu (if 1, then view_menu())
    print("1. View Menu")
    print("2. Place an order")
    print("3. Sign Up for Loyalty Program")
    print("4. View Loyalty Account")
    print("5. View All Loyalty Members")
    print("6. View Sales Statistics")
    print("7. Exit")
    

#FOR CHOICE == 1
def view_menu():
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


#FOR CHOICE == 2
def take_order():
    total_price = 0 #SHOULD BE OUTSIDE BRUH
    total_orders = []
    
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
    
    while True:
        order_code = input("Enter your order code: ")
        
        if len(order_code) != 3: #if not equal to 3
            print("Invalid order code. Please ensure the code follows the format [Category][Item][Size], e.g. E2L")
            continue

        order_category = order_code[0]
        order_drink = order_code[1]
        order_size = order_code[2]
            
        if order_category == "E" or order_category == "N" or order_category == "F":      
            if order_drink in menu[order_category]:   
                if order_size == "S" or order_size == "M" or order_size == "L":
                    
                    drink = menu[order_category][order_drink]
                    drink_size = sizes[order_size]["price"]
                    drink_price = drink["price"] + drink_size
                    total_price = total_price + drink_price
                    
                    total_orders.append({"name": drink["name"],
                                         "size": sizes[order_size]["size"],
                                         "price": drink_price
                    })
                    
                    print()
                    print(f"Added: {drink['name']} ({sizes[order_size]['size']}) - ${drink_price} ")
                    print()
                    
                    while True: #so that if the user inputs something other than yes or no, it will ask again if they want to add another order
                        order_more = input("Anything else? (Yes/No): ")

                        if order_more == "Yes" or order_more == "yes":
                            break
                        elif order_more == "No" or order_more == "no":
                            break
                        else:
                            print("Invalid input. Please enter yes or no.")
                            print(order_more)
                    if order_more == "Yes" or order_more == "yes":
                        continue
                    elif order_more == "No" or order_more == "no":
                        break
                    #break
                
                else:
                    print("Invalid size letter!")          
            else:
                print("Invalid drink category!")
        else:
            print("Invalid drink category!")
    
    print()
    print("RECEIPT")
    for item in total_orders:
        print(f"{item['name']} ({item['size']}): ${item["price"]} ")
    print(f"Total: ${total_price}")
    
    points_earned = total_price/10
    print(f"Points earned: {points_earned}")
    
    print("New points balance: ")
    print()

#CALLING ALL FUNCTIONS UGH SO SATISFYING
print("Welcome to Katipunan Grind")
print()
main_menu()
print()
choice = int(input("Enter your choice: "))

if choice == 1:
    print()
    view_menu()
    print()
    main_menu()
    choice = int(input("Enter your choice: "))
    

if choice == 2:
    take_order()


if choice == 7:
    print("Thank you for visiting Katipunan Grind!")
    exit()



    
    
    
    
    

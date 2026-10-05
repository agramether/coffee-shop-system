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

print(menu["E"]["1"] ["name"])

                

def take_order():
    total_price = 0 #SHOULD BE OUTSIDE BRUH
    total_orders = []
    
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
                    print(f"Added {drink['name']} ({sizes[order_size]['size']}) - ${drink_price} ")
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
    print("Points earned: ")
    print("New points balance: ")
    print()
        
take_order()


    
                


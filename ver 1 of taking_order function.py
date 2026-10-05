#sept 16, 2026
#ver 1 of def take_orders using nested conditionals
#pls try again part doesnt work if user input only has one error for one part
#had to redo using a while loop na lang and then have it break once price is calculated at the end
#realizations: i don't like when i have to redo an entire block of code uhhhh

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

sizes = {"S": {"size": "Small", "add_on": 0},
         "M": {"size": "Medium", "add_on": 25},
         "L": {"size": "Large", "add_on": 50}
         }

def take_order():
    order_code = input("Enter your order code: ")

    if len(order_code) == 3:
        order_category = order_code[0]
        order_drink = order_code[1]
        order_size = order_code[2]
    
        if order_category == "E" or order_category == "N" or order_category == "F":
            print("Drink category is valid! Processing your order...") #just to check if 3-letter code is valid. remove later
        
            if order_drink in menu[order_category]:
                print("Drink is valid and in the menu. Processing your order...")
            
                if order_size == "S" or order_size == "M" or order_size == "L":
                    print("Order size coming up! Processing your order....")
                
                    drink = menu[order_category][order_drink]
                    drink_size = sizes[size]["add_on"]
                    drink_price = drink["price"] + add_on
                
                    print(f"Drink: {drink['name']}")
                    print(f"Size: {sizes[size]['name']}")
                    print(f"Total: ${drink_price}")
                
                else:
                    print("Invalid size letter!")
                    print()
                    take_order()
                
            else:
                print("Invalid drink code!")
                print()
                take_order()
            
        else:
            print("Invalid drink category!")
            print()
            take_order()
    else:
        print("Order code must have 3 characters. Please try again")
        print()
        take_order() #recursive function calls. would be better to use a while loop instead and then break once price is calculated at the end


take_order()

    
                
#ver1 of coffee shop ordering system
#sept 15, 2026
#ver2 of coffee shop ordering system
#oct 4, 2026 (moved to vscode)


from secrets import choice


def main_menu (): #SYSTEM: then function for each so that when user inputs 1, it calls the function for main menu (if 1, then view_menu())
    print("Welcome to Katipunan Grind")
    print("1. View Menu")
    print("2. Place an order")
    print("3. Sign Up for Loyalty Program")
    print("4. View Loyalty Account")
    print("5. View All Loyalty Members")
    print("6. View Sales Statistics")
    print("7. Exit")
    
    print()
    choice = int(input("Enter your choice: "))

    if choice == 7:
        print("Thank you for visiting Katipunan Grind!")
        exit()
    
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


        def take_order():
            while True:
                order_code = input("Enter your order code: ")

                if len(order_code) != 3:
                    print("Invalid order code! Please try again.")
                    continue

                order_category = order_code[0]
                order_drink = order_code[1]
                order_size = order_code[2]

                if order_code == "E" or order_code == "N" or order_code == "F":
                    print("Order size is valid. Processing your order...")
                
                    
    if choice == 1:
        print("*****KATIPUNAN GRIND*****")
        print()
        view_menu()

        

    #if choice == 2:
        #ordering()

    if choice == 3:
        database = []
        
        
        print("*****KATIPUNAN GRIND*****")
        print()
        name = str(input("Enter your name: "))
        
        
        
        if name in database:
            print(f"Welcome {name}! Your loyalty member ID is {mem_ID}")
            
            
            main()
            
main_menu()


    
    
    
    
    

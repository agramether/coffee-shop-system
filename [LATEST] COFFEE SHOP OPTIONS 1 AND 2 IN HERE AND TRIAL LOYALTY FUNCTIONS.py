#copy pasted all the code with functioning options 1 & 2
#to do the remaining loalty functionalities
#ugh

#ver1 of coffee shop ordering system
#sept 15, 2026
#ver2 of coffee shop ordering system
#oct 4, 2026 (moved to vscode)


def main_menu (): #then function for each so that when user inputs 1, it calls the function for main menu (if 1, then view_menu())
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
        print(f" E{i:<2}   ${menu['E'][i]['price']:<3}   {menu['E'][i]['name']} ")  #for price of i in number i of key E
    print("NON-COFFEE")
    for i in menu["N"]:
        print(f" N{i:<2}   ${menu['N'][i]['price']:<3}   {menu['N'][i]['name']} ")  #for name of drink i in key N
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
    points_balance = 100
    
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
        
    while True: #so that if the user inputs something other than yes or no, it will ask again if they are a loyal member or not
        loyal_customer = input("Are you a loyal customer? (Yes/No): ")

        if loyal_customer == "Yes" or loyal_customer == "yes":
            break
        elif loyal_customer == "No" or loyal_customer == "no":
            break
        else:
            print("Invalid input. Please enter yes or no.")
            print()
            
    if loyal_customer == "Yes" or loyal_customer == "yes":
        member_id = input("Enter your member ID: ")
        if member_id in customer_list:
            print("Member ID found. Welcome!")
    elif loyal_customer == "No" or loyal_customer == "no":
        print("Please register first.")
    else:
        print("Invalid input. Please try again.")
    
    
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
                            break                      #proceed to the next outside conditional
                        elif order_more == "No" or order_more == "no":
                            break
                        else:
                            print("Invalid input. Please enter yes or no.")
                            print()
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
    
    points_balance = points_balance - points_earned
    print(f"New points balance: {points_balance} ")
    print()

loyal_customers = [] #so that when another customer tries to sign up, the list is updated since it's global 
total_points = []
total_balance = []
loyal_ids = []

#FOR CHOICE == 3
def signup_loyalty():
    customer_name = input("Enter your name: ")
    loyal_customers.append(customer_name)
    total_points.append(0)
    total_balance.append(0)
    member_id = f"M00{len(loyal_customers)}" #dapat galing sa kung ilan loyal customers 
    loyal_ids.append(member_id)
    print()
    
    for i in range(len(loyal_customers)):
        print(f"Welcome, {customer_name}! Your loyalty member ID is {member_id}.")
        print()

#FOR CHOICE == 4
def view_loyalty():
    member_id = input("Enter member ID: ")
    
    if member_id in loyal_ids:
        
        for i in range(len(loyal_ids)):
            
            if member_id == loyal_ids[i]:
                print()
                print("LOYALTY ACCOUNT")
                print(f"Name: {loyal_customers[i]}")
                
                if total_points[i] > 300:  #total_points of each so with [i]
                    tier = "Gold"
                elif total_points[i] > 100 and total_points[i] < 300:
                    tier = "Silver"
                elif total_points[i] < 100 and total_points[i] >= 0:
                    tier = "Regular"
                
                print(f"Tier: {tier}")
                print(f"Total Points Earned: {total_points[i]} ")
                print(f"Points Balance: {total_balance[i]}")
                
                if total_points[i] >= 100:
                    redeem_points = input("Redeem 100 points for a free Small drink? (Yes/No): ")
                    
                    if redeem_points == "Yes" or redeem_points == "yes":
                        print("Redeemed 100 points. Enjoy a free Small drink of your choice on your next visit!")
                        print(f"New points balance: {total_balance - 100}")
                    elif redeem_points == "No" or redeem_points == "no":
                        print("You did not redeem any points.")
    else:
        print("Member ID not found.")
    
    
#FOR CHOICE == 5
def display_loyalty():
    print("ALL LOYALTY MEMBERS")
    
    for i in range(len(loyal_customers)):
        if total_points[i] > 300:  #total_points of each so with [i]
            tier = "Gold"
        elif total_points[i] > 100 and total_points[i] < 300:
            tier = "Silver"
        elif total_points[i] < 100 and total_points[i] >= 0:
            tier = "Regular"
        print(f"M00{i+1}  {loyal_customers[i]:<20} {tier:>10} Total Earned: {total_points[i]:<3} Balance: {total_balance[i]:<3}  ")

    
##################################################
print("Welcome to Katipunan Grind")
while True:
    print()
    main_menu()
    print()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print()
        view_menu()
        print()
        #main_menu()
        #choice = int(input("Enter your choice: "))
        
    elif choice == "2":
        take_order()
        
    elif choice == "3":
        signup_loyalty()
        
    elif choice == "4":
        view_loyalty()
        
    elif choice == "5":
        display_loyalty()
        
        
    #elif choice == "6":
    
    elif choice == "7":
        print("Thank you for visiting Katipunan Grind!")
        break
    
    else:
        print("Invalid input. Please enter a number from 1-7.")





    
    
    
    
    


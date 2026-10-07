# Bea Margareth G. Claveria, 245382
# October 7, 2026

# I certify that this submission complies with the DISCS Academic Integrity
# Policy and the specifications of this course requirement.

# If I have discussed my/our Python language code with anyone other than
# my instructor(s), my groupmate(s), the teaching assistant(s),
# the extent of each discussion has been clearly noted along with a proper
# citation in the comments of my/our program.

# If any Python language code or documentation used in my/our program
# was obtained from another source, either modified or unmodified, such as a
# textbook, website, genaI tool, or another individual, the extent of its use has been
# clearly noted along with a proper citation in the comments of my/our program.

################################################################################

# Cite your sources here, if any.
# No need for any formal citation format.
# If use of GenAI tools is allowed for this requirement, 
#   please provide either a list of the prompts used
#   or a link to the conversation.

#more practice for accessing items in nested dictionaries for implementation of menu: https://www.w3schools.com/python/python_dictionaries_nested.asp
#canvas slides for dictionaries and for going back to the fundamentals of functions and scope of names because i had a hard time with indentations most of the time TT
#w3schools for how to add specific number of space between strings for displaying menu with proper alignment: https://www.w3schools.com/python/python_string_formatting.asp

################################################################################
#ver1 of coffee shop ordering system
#sept 15, 2026 (menu created with lists)
#sept 16, 2026 (options 1-3 functional)
#ver2 of coffee shop ordering system
#sept 26, 2026 (changed menu list to dictionary list)
#ver3 of coffee shop ordering system
#oct 4, 2026 (finished menu and ordering)
#oct 5, 2026 (12345 functioning but still errors for printing receipt for guests)
#oct 6, 2026 (trying to do bonus part)
#oct 7, 2026 (finalized bonus part)

loyal_customers = [] #so that when another customer tries to sign up, the list is updated since it's global 
total_points = []    #current points from that order only
points_balance = []  #total points across all orders
loyal_ids = []

total_price = 0
total_orders = []
points_earned = 0

#for stats
loyal_orders = []
guest_orders = []
espresso_orders = []
noncoffee_orders = []
frappe_orders = []
total_revenue = []

def main_menu (): #function for each so that when user inputs the number, it calls the corresponding function 
    print("MAIN MENU")
    print("   1. View Menu")
    print("   2. Place an order")
    print("   3. Sign Up for Loyalty Program")
    print("   4. View Loyalty Account")
    print("   5. View All Loyalty Members")
    print("   6. View Sales Statistics")
    print("   7. Exit")
    
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
        print(f" E{i:<2}   ${menu['E'][i]['price']:<3}   {menu['E'][i]['name']} ")  #for price of i in drink i of key E
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
    
    customer_count = 0
    
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
    
    #check if loyal member
    while True:
        loyal_customer = input("Are you a loyal customer? (Yes/No): ")
        
        if loyal_customer == "Yes" or loyal_customer == "yes":
            member_id = input("Enter your member ID: ")
            
            if member_id in loyal_ids:
                for i in range(len(loyal_ids)):
                    if member_id == loyal_ids[i]:
                        customer_count = i    #assign to i so that it looks for the customer's position in the list when taking multiple orders from the same member ID
                        print(f"Member ID found. Welcome {loyal_customers[i]}!")
                        break #PARA WALANG INFINITE LOOP AND MAG BREAK HERE TO PROCEED SA ORDERING PART
                break #DITO DIN
            else:
                print("Member ID not found. Please try again.")
        
        elif loyal_customer == "No" or loyal_customer == "no":
            signup = input("Would you like to sign up for the loyalty program? (Yes/No): ")
            
            if signup == "No" or signup == "no":
                break                                  #exit checking loyalty loop and proceed to order loop
            elif signup == "Yes" or signup == "yes":
                signup_loyalty()
                loyal_customer = "Yes"
                member_id = loyal_ids[-1] #get last member ID in list (ung kaka-reg lang) huhu 
                customer_count = len(loyal_ids) - 1   #for index of newly registered customer #MINUS DAPAT
                break
            
            else:
                print("Invalid input. Please enter Yes or No.")
        
        else:
            print("Invalid input. Please enter Yes or No.")
            print()

    #ordering part
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
                    
                    drink = menu[order_category][order_drink] #calls the corresponding index directly
                    drink_size = sizes[order_size]["price"]
                    drink_price = drink["price"] + drink_size
                    
                    total_orders.append({"name": drink["name"],
                                         "size": sizes[order_size]["size"],
                                         "price": drink_price
                    })
                    
                    print()
                    print(f"Added: {drink['name']} ({sizes[order_size]['size']}) - ${drink_price} ")
                    print()
                    
                    #for stats
                    if order_category == "E":
                        espresso_orders.append(1)
                    elif order_category == "N":
                        noncoffee_orders.append(1)
                    elif order_category == "F":
                        frappe_orders.append(1)
                    
                    #for asking if add another order
                    while True:
                        order_more = input("Anything else? (Yes/No): ")
                        
                        if order_more == "No" or order_more == "no":
                            break  #exits only the if asking for another order part 
                        elif order_more == "Yes" or order_more == "yes":
                            print()  
                            break    #to exit loop for asking for anything else and proceed to loop for ordering again
                        else:
                            print("Invalid input. Please enter Yes/No.")
                    
                    if order_more == "No" or order_more == "no":   #to actually exit from entire ordering loop
                        break
                
                else:
                    print("Invalid letter for size!")          
            else:
                print("Invalid drink in category!")
        else:
            print("Invalid drink category!")
        
    if loyal_customer == "Yes" or loyal_customer == "yes": #SA LABAS PA DAPAT 
        loyal_orders.append(1)
    else:
        guest_orders.append(1)   
    
    #calculation for loyalty system
    total_price = 0  
    
    for i in range(len(total_orders)):
        total_price = total_price + total_orders[i]["price"] #add to the total price the corresponding price of item i
    
    points_earned = total_price / 10
    
    #para ma-update ung points sa global and para mag-update if they order again
    if loyal_customer == "Yes" or loyal_customer == "yes":  
        for i in range(len(loyal_ids)):
            if member_id == loyal_ids[i]:
                total_points[i] = total_points[i] + points_earned #total_points stores the total for that customer and points_earned is just the points from CURRENT transaction 
                points_balance[i] = points_balance[i] + points_earned
    
    return customer_count, loyal_customer

#FOR CHOICE == 3
def signup_loyalty():
    customer_name = input("Enter your name: ")
    loyal_customers.append(customer_name)
    total_points.append(0)
    points_balance.append(0)
    member_id = f"M00{len(loyal_customers)}" #dapat galing sa kung ilan loyal customers 
    loyal_ids.append(member_id)
    
    print()
    print(f"Welcome, {customer_name}! Your loyalty member ID is {member_id}.")
    print()

#FOR CHOICE == 4
def view_loyalty():
    while True:
        member_id = input("Enter member ID: ")
        
        #check if each customer is in loyal ids
        if member_id in loyal_ids:
            break
        else:
            print("Member ID not found.")
    
    #get each customer and print their details
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
            print(f"Points Balance: {points_balance[i]}")
            
            #for redeeming points 
            if points_balance[i] >= 100: 
                redeem_points = input("Redeem 100 points for a free Small drink? (Yes/No): ")
                    
                if redeem_points == "Yes" or redeem_points == "yes":
                    points_balance[i] = points_balance[i] - 100   
                
                    print()
                    print("Redeemed 100 points. Enjoy a free Small drink of your choice on your next visit!")
                    print(f"New points balance: {points_balance[i]}")
            
                elif redeem_points == "No" or redeem_points == "no":
                    print("You did not redeem any points.")
       
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
        print(f"M00{i+1}  {loyal_customers[i]:<20} {tier:>10} Total Earned: {total_points[i]:<3} Balance: {points_balance[i]:<3}  ")

#FOR CHOICE 6
def shop_stats():
    total_drinks_count = len(espresso_orders) + len(noncoffee_orders) + len(frappe_orders) #DRINKS LANG, NOT INCLUDING LOYAL OR UNLOYAL CUSTOMERS
    
    count_loyalty_sold = len(loyal_orders)
    percent_loyalty_sold = round((count_loyalty_sold / total_drinks_count)*100, 1)
    
    count_guest_sold = len(guest_orders)
    percent_guest_sold = round((count_guest_sold / total_drinks_count)*100, 1)
    
    count_espresso_sold = len(espresso_orders)
    percent_espresso_sold = round((count_espresso_sold / total_drinks_count)*100, 1)
    
    count_noncoffee_sold = len(noncoffee_orders)
    percent_noncoffee_sold = round((count_noncoffee_sold / total_drinks_count)*100, 1)
    
    count_frappe_sold = len(frappe_orders)
    percent_frappe_sold = round((count_frappe_sold / total_drinks_count)*100, 1)
    
    amount_total_revenue = 0
    for i in range(len(total_revenue)):   
        amount_total_revenue = amount_total_revenue + total_revenue[i] #to add all the previous revenue
    
    total_orders_count = len(loyal_orders) + len(guest_orders) #LOYAL AND GUESTS COUNT ONLY!
    
    print(f"Total Orders: {total_orders_count}")
    print(f"Total Revenue: ${amount_total_revenue} ")
    print(f"Loyalty Member Orders: {count_loyalty_sold} ({percent_loyalty_sold}%) ")
    print(f"Guest Orders: {count_guest_sold} ({percent_guest_sold}%)")
    print(f"Total Drinks: {total_drinks_count}")
    print(f"Espresso-Based Drinks: {count_espresso_sold} ({percent_espresso_sold}%)")
    print(f"Non-Coffee Drinks: {count_noncoffee_sold} ({percent_noncoffee_sold}%)")
    print(f"Frappe Drinks: {count_frappe_sold} ({percent_frappe_sold}%)")
    
####################################################################################################################################################
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
        
    elif choice == "2":
        total_orders = [] #already declared in global but declare here again so that when same user orders again, it can be counted as another index for the second receipt and para maupdate ung poitns
        customer_count, loyal_customer = take_order()  
        
        print()
        print("RECEIPT")
        
        #calculation for receipt (did this earlier also)
        total_price = 0
        
        for i in range(len(total_orders)):
            print(f"{total_orders[i]['name']} ({total_orders[i]['size']}): ${total_orders[i]["price"]} ")
            total_price = total_price + total_orders[i]["price"] #price of each order in total_orders list
            
        print(f"Total: ${total_price}")
        total_revenue.append(total_price) #to update for stats
        
        if loyal_customer == "Yes" or loyal_customer == "yes":
            points_earned = total_price/10
            print(f"Total points earned: {points_earned}")
            print(f"New points balance: {points_balance[customer_count]}")
        print()
        
    elif choice == "3":
        signup_loyalty()
        
    elif choice == "4":
        view_loyalty()
        
    elif choice == "5":
        display_loyalty()
            
    elif choice == "6":
        shop_stats()
    
    elif choice == "7":
        print("Thank you for visiting Katipunan Grind!")
        break
    
    else:
        print("Invalid input. Please enter a number from 1-7.")

menu = {"E1 - Americano (Espresso-Based)": "Php 120",
        "E2 - Latte (Espresso-Based)": "Php 125",
        "E3 - Spanish Latte (Espresso-Based)": "Php 130",
        "N1 - Chocolate (Non-Coffee)": "Php 115",
        "N2- Hojicha (Non-Coffee)": "Php 135",
        "F1 - Mocha Frappe (Frappe/Blended)": "Php 150",
        "F2 - Caramel Frappe (Frappe/Blended)": "Php 155"
    }
    

def get_order():
    
    order = []

    order_received = input("Enter order code: ")
    order.append(order_received)
    print(order)
    category = order[0][0] #first 0 is for the first element of the order (E1S), so to get just the first letter for order code, add another [0]
    item_num = order[0][1]
    size = order[0][2]
    print()
    print(category)
    print(item_num)
    print(size)
    print("Anything else? ")
    
    #def add_order():

get_order()
 


#return_category =
#return_item_num =
#return_size = 

#print(Added: {}{}



#def add_another_order ():
    








#print(f"Your final order code is: {order_category[0]}")
#if len(order_category) > 2:
    #print("Please input a three-letter code to begin your purchase.")


#full_order = input(f"{category}{number}{size}")




    
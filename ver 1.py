#ver 1 of coffee shop ordering system
#sept 15, 2026

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
        menu = {"E1 - Americano (Espresso-Based)": "Php 120",
                "E2 - Latte (Espresso-Based)": "Php 125",
                "E3 - Spanish Latte (Espresso-Based)": "Php 130",
                "N1 - Chocolate (Non-Coffee)": "Php 115",
                "N2 - Hojicha (Non-Coffee)": "Php 135",
                "F1 - Mocha Frappe (Frappe/Blended)": "Php 150",
                "F2 - Caramel Frappe (Frappe/Blended)": "Php 155"        
                }
        for key, value in menu.items():
            print(f"{key}: {value}")
    
    if choice == 1:
        print("*****KATIPUNAN GRIND*****")
        print()
        view_menu()
        #print()
        #main_menu()
        

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


    
    
    
    
    
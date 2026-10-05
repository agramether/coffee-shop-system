#for loyalty shit


loyal_customers = ["margaux", "columbina", "sandrone", "arle", "childe", "pantalone"] #so that when another customer tries to sign up, the list is updated since it's global 
total_points = [180, 150, 54, 45, 180, 56]
total_balance = [20, 34, 54, 78, 67, 90]
loyal_ids = []

def signup_loyalty():
    customer_name = input("Enter your name: ")
    loyal_customers.append(customer_name)
    total_points.append(0)
    total_balance.append(0)
    print()
    print(f"Loyal customers: {loyal_customers}")
    print(f"Total points: {total_points}")
    print(f"Total balance: {total_balance}")
    
    print()

def display_loyalty():
    print("ALL LOYALTY MEMBERS")
    for i in range(len(loyal_customers)):
            #print(f"Welcome, {customer_name}! Your loyalty member ID is M00{len(loyal_customers)}.")
            #print()
        if total_points[i] > 300:  #total_points of each so with [i]
            tier = "Gold"
        elif total_points[i] > 100 and total_points[i] < 300:
            tier = "Silver"
        elif total_points[i] < 100:
            tier = "Regular"
        print(f"M00{i+1}  {loyal_customers[i]:<15} {tier:>7} Total Earned: {total_points[i]:<3} Balance: {total_balance[i]:<3}  ")

signup_loyalty()
display_loyalty()
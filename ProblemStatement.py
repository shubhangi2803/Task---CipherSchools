# Dictionary to store Item name as key and its weight and price as its value
groceryList = {}

# Input: Budget
while True:
    try:
        budget = int(input("Enter your budget: "))
        break
    except:
        print("Please enter correct value of budget.")

while True:
    print("1. Add an item")
    print("2. Exit")

    # Input: Choice
    while True:
        try:
            choice = int(input("Enter your choice: "))
            break
        except:
            print("Please enter correct choice.")
    
    # Choice: To add product
    if choice == 1:
        # Input: Product, Quantity, Amount 
        while True:
            try:
                pro = input("Enter product: ")
                qty = float(input("Enter quantity: "))
                amt = int(input("Enter price: "))
                break
            except:
                print("Please enter all values correctly.")
        
        # Price exceeding current budget
        if amt > budget:
            print("Can't buy the product as budget left is : ",budget)
            continue
        
        else:
            # Already existing product
            if pro in groceryList:
                groceryList[pro][0] = qty
                budget += groceryList[pro][1]
                groceryList[pro][1] = amt
            # New product
            else:
                groceryList[pro] = [qty, amt]

        # Remaining budget
        budget -= amt
    
    # Choice: To Exit
    elif budget == 0 or choice == 2:
        break

    # Remaining budget
    print("Amount left: ",budget)

# Things that can be bought with remaining budget
canBuy = []    
for key,val in groceryList.items():
    if val[1] <= budget:
        budget -= val[1]
        canBuy.append(key)
    if budget == 0:
        break

toBuy = "Amount left can buy you "
for item in canBuy:
    toBuy += item + " "
if toBuy != "Amount left can buy you ":
    print(toBuy)

# Printing Grocery List
print("GROCERY LIST is: ")

# Empty Grocery List
if not groceryList:
    print("Empty List !")
else:
    print ("{:<15} {:<15} {:<15}".format('Product Name', 'Quantity', 'Price'))
    for key, value in groceryList.items():
        print ("{:<15} {:<15} {:<15}".format(key,value[0],value[1]))

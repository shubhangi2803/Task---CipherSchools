groceryList = {}

while True:
    try:
        budget = int(input("Enter your budget: "))
        break
    except:
        print("Please enter correct value of budget.")

while True:
	print("1. Add an item")
	print("2. Exit")
    while True:
        try:
        	choice = int(input("Enter your choice: "))
            break
        except:
            print("Please enter correct choice.")

	if choice == 1:
        while True:
            try:
                pro = input("Enter product: ")
                qty = float(input("Enter quantity: "))
                amt = int(input("Enter price: "))
                break
            except:
                print("Please enter all values correctly.")

		if amt > budget:
			print("Can't buy the product as budget left is : ",budget)
            continue

		else:
			if pro in groceryList:
				groceryList[pro][0] = qty
				budget += groceryList[pro][1]
				groceryList[pro][1] = amt
			else:
				groceryList[pro] = [qty, amt]
			budget -= amt

	elif budget == 0 or choice == 2:
		break
	print("Amount left: ",budget)

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

print("GROCERY LIST is: ")
if not groceryList:
    print("Empty List !")
else:
    print ("{:<15} {:<15} {:<15}".format('Product Name', 'Quantity', 'Price'))
    for key, value in groceryList.items():
        print ("{:<15} {:<15} {:<15}".format(key,value[0],value[1]))

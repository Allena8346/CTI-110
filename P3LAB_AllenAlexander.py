#Alexander Allen
#23Oct24
#P3LAB
#Getting the correct change using if else

#Get value from user
change = float(input("Enter the amount of money as a float: $"))
#print(f"Change Amount: {change}")

#Converting the value to an integer
change = int(change * 100)
#print(f"Change Amount: {change}")

#Determine how many coins are needed
num_dollars = change //100
change = change - (num_dollars * 100)

num_quarters = change //25
change = change - (num_quarters * 25)

num_dimes = change //10
change = change - (num_dimes * 10)

num_nickels = change //5
change = change - (num_nickels * 5)

num_pennies = change


#money = money - (nickels * 5)
#Get pennies from money amount
#pennies = money
#print(f"Pennies: {pennies}")

if change == 0:
    print("No change")
if num_dollars >= 1:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else: #more than one dollar
        print(f"{num_dollars} Dollars")

if num_quarters >= 1:
    if num_quarters == 1:
        print(f"{num_quarters} Quarter")
    else: #more than one quarter
        print(f"{num_quarters} Quarters")

if num_dimes >= 1:
    if num_dimes == 1:
        print(f"{num_dimes} Dime")
    else: #more than one dime
        print(f"{num_dimes} Dimes")

if num_nickels >= 1:
    if num_nickels == 1:
        print(f"{num_nickels} Nickel")
    else: #more than one nickel
        print(f"{num_nickels} Nickels")

if num_pennies >= 1:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
    else: #more than one penny
        print(f"{num_pennies} Pennies")

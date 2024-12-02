#Alexander Allen
#13NOV24
#P5LAB
#Simulate self-checkout using function

#Import the random library to use in program
import random

def disperse_change(change):
    print(f"Change is: ${change:.2f}")
    print()
    #Converting the value to an integer
    change = int(round(change * 100, 2))

    if change == 0:
        print("No change")

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

    
    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} Dollar")
        else: #more than one dollar
            print(f"{num_dollars} Dollars")

    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} Quarter")
        else: #more than one quarter
            print(f"{num_quarters} Quarters")

    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} Dime")
        else: #more than one dime
            print(f"{num_dimes} Dimes")

    if num_nickels > 0:
        if num_nickels == 1:
            print(f"{num_nickels} Nickel")
        else: #more than one nickel
            print(f"{num_nickels} Nickels")

    if num_pennies > 0:
        if num_pennies == 1:
            print(f"{num_pennies} Penny")
        else: #more than one penny
            print(f"{num_pennies} Pennies")






#define main function
def main():
    print("Welcom to the store")
    #Generate money owed
    owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${owed:.2f}")
    inPut = float(input("How much cash will you put in the self-checkout? $"))
    change = inPut - owed
    change = round(change, 2)
    #print(change)
    
    #Call the function as coins
    disperse_change(change)
    
#Call the main
if __name__ == "__main__":
    main()


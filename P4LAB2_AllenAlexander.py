# Alexander Allen
# 30Oct24
# P4LAB2
# Use Loops (for & while) to make a multiplication table of numbers greater than 0

#Create variable to make program run first time
run_again = "yes"

#While loop to control entire program
while run_again == "yes":
    #Get input from user
    userNum = int(input("Enter an integer: "))
    print()
    #Check if userNum is positive
    if userNum >= 0:
        #Loop to print multiplication
        for num in range(1,13):
            print(userNum, "*" ,num, "=", userNum * num)
            #print(f"{userNum} * {num} = {userNum*num}")
    # If userNum is negative, tell the user
    else:
        print("Program does not handle negative numbers!")
    print()
    run_again = input("Would you like to run the program again (yes/no)? ").lower()
    print()

#Loop Breaks
print("Exiting Program....")

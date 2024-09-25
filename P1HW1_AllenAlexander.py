#Alexander Allen
#16Sep24
#P1HW1
#Useing math expressions with a user input

#print() makes an empty print line
print('-----Calculating Exponents-----')

print()
print()

#Get input from user
baseValue = input('Enter an integer as the base value: ')
exponent = input('Enter an integer as the exponent: ')

# Convert baseValue and exponent to integer
# baseValue = int(input('Enter an integer as the base value: '))
# exponent = int(input('Enter an integer as the exponent: '))
baseValue = int(baseValue)
exponent = int(exponent)

print()
print()

#Display results to the user
print(baseValue, 'raised to the power of', exponent, 'is', baseValue**exponent, '!!' )

print()
print()

print('-----Addition and Subtraction-----')

print()
print()

#Get Starting integer from user
startingInt = input('Enter a starting integer: ')
intAdd = input('Enter an integer to add: ')
intSub = input('Enter an integer to subtract: ')

# Convert startingInt, intAdd, and intSub to integer
startingInt = int(startingInt)
intAdd = int(intAdd)
intSub = int(intSub)
result = startingInt + intAdd - intSub
print()
print()


#Display results to the user
print(startingInt, '+', intAdd, '-', intSub, 'is equal to', result )

#Alexander Allen
#25Sep24
#P1HW2
#Travel Plan and outline

print('This program calculates and displays travel expenses')

print()

budget = int(input('Enter Budget: '))
dest = input('Enter your travel destination: ')
gas = int(input('How much do you think you will spend on gas? '))
shelter = int(input('Approximately, how much will you need for accomodation/hotel? '))
food = int(input('Last, how much do you need for food? '))
expenses = gas + shelter + food
result = budget - expenses

print()

print('----------Travel Expenses----------')
print('Location:', dest)
print('Initial Budget:', budget)
print()
print('Fuel:', gas)
print('Accomodation:', shelter)
print('Food:', food)
print('Remaining Balance:',result)

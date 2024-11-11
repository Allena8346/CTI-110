#Alexander Allen
#02Oct24
#P2LAB2
#Using Dictionary


#print() makes an empty print line or adding '\n' to the begining or end to get an empty line above or below


#Create a dictionary using key:value pairs
cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

print(cars.keys(), '\n')

#Get a car from the user
userCar = (input("Enter a vehicle to see it's mpg: "))
print()

#Dispaly mpg for userCar
print(f"The {userCar} gets {cars[userCar]} mpg.")
print()
mpg = float(input(f"How many miles will you drive the {userCar}? "))
print()

#Calculate Gallons of gas needed
gallons_needed = mpg/cars[userCar]

print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {userCar}", mpg, "miles.")









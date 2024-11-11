#Alexander Allen
#30Sep24
#P2HW1
#Using imported library, math, and f-string

# Import math library
import math

#print() makes an empty print line or adding '\n' to the begining or end to get an empty line above or below

#Variables
radius = float(input('What is the radius of the circle? '))
x = math.pi
diameter = 2 * radius
circumference = 2 * x * radius
area = x * math.pow(radius, 2)

#Display diameter with one decimal place.
print('\n'f'The diameter of the circle is {diameter:.1f}''\n')
print (f'The circumference of the circle is {circumference:.2f}''\n')
print (f'The area of the circle is {area:.3f}')

#Prints calculated information

#print ('\n''The diameter of the circle is', round(diameter,1),'\n')
#print ('The circumference of the circle is', round(circumference,2),'\n')
#print ('The area of the circle is', round(area,3))


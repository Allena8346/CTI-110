#Alexander Allen
#09Oct24
#P2HW2
#A Report Card that displays the highest, lowest, sum, and average grades.

#print() makes an empty print line

# Convert Mod{1..6} to float
# Mod1 = int(input('Enter grade for Module 1: '))
# Mod6 = int(input('Enter grade for Module 6: '))

Mod1 = float(input(f"Enter grade for Module 1: "))
Mod2 = float(input("Enter grade for Module 2: "))
Mod3 = float(input("Enter grade for Module 3: "))
Mod4 = float(input("Enter grade for Module 4: "))
Mod5 = float(input("Enter grade for Module 5: "))
Mod6 = float(input("Enter grade for Module 6: "))
list1 = [Mod1,Mod2,Mod3,Mod4,Mod5,Mod6]
#low = min(Mod1,Mod2,Mod3,Mod4,Mod5,Mod6)
low = min(list1)
#high = max(Mod1,Mod2,Mod3,Mod4,Mod5,Mod6)
high = max(list1)
Sum = Mod1 + Mod2 + Mod3 + Mod4 + Mod5 + Mod6
Avg = Sum / len(list1)

print('-----Results-----')
print(f"{'Lowest Grade: ':<15}{low:.1f}")
print(f"Highest Grade: {high:.1f}")
print(f"Sum of Grades: {Sum:.1f}")
print(f"{'Average: ':<15}{Avg:.2f}")
print("--------------------------")

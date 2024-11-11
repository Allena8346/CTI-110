# Alexander Allen
#10NOV24
#P4HW1
#Calculate scores and orginize them

#Get number of scores
num_scores = int(input("How many scores do you want to enter? "))

inList = range(0, 100)

#Empty List to hold valid items
scores = []

# For loop to allow user to enter items
for List in range(num_scores):
    score = float(input(f"Enter score #{List + 1}: "))
    while score < 0 or score > 100:
        print()
        print(f"INVALID Score entered!!!!")
        print(f"Score should be between 0 and 100")
        score = float(input(f"Enter score #{List + 1} again: "))
    scores.append(score)
        
#Lowest Score
lowest_score = scores[0]
for score in scores:
    if score < lowest_score:
        lowest_score = score

#Modified List
modified_scores = []
found = False
for score in scores:
    if score == lowest_score and not found:
        found = True
    else:
        modified_scores.append(score)

#Average
total = 0
for score in modified_scores:
    total += score
average_score = total / len(modified_scores)

#Letter Grades
if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'


print()
print("----------Results----------")
print(f"Lowest Score : {lowest_score}")
print(f"Modified List : {modified_scores}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade : {grade}")
print("---------------------------")

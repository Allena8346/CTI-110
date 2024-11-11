# Ask the user for the number of scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))

# Initialize an empty list to store scores
scores = []

# Use a for loop to collect each score
for i in range(num_scores):
    while True:
        score = float(input(f"Enter score #{i + 1}: "))
        if 0 <= score <= 100:
            scores.append(score)
            break
        else:
            print("INVALID Score entered! Score should be between 0 and 100.")

# Find the lowest score
lowest_score = scores[0]
for score in scores:
    if score < lowest_score:
        lowest_score = score

# Create a modified list without the lowest score
modified_scores = []
found = False # To remove only the first occurrence of the lowest score
for score in scores:
    if score == lowest_score and not found:
        found = True # Skip the first occurrence of the lowest score
    else:
        modified_scores.append(score)

# Calculate the average of the modified list
total = 0
for score in modified_scores:
    total += score
average_score = total / len(modified_scores)

# Determine the letter grade based on the average score
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

# Display results
print("\n------------ Results ------------")
print(f"Lowest Score : {lowest_score}")
print(f"Modified List : {modified_scores}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade : {grade}")
print("---------------------------------")

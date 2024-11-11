# Your Name
# Date
# Assignment Name
# A brief description of the project

# Get input from user
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate overtime
overtime_hours = max(0, hours_worked - 40)
regular_hours = hours_worked - overtime_hours
overtime_pay = overtime_hours * pay_rate * 1.5
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Display output
print("\nEmployee name:", employee_name)
print("---------------------------------------------------------")
print(f"{'Hours Worked':<15} {'Pay Rate':<10} {'OverTime':<10} {'OverTime Pay':<15} {'RegHour Pay':<15} {'Gross Pay':<15}")
print("---------------------------------------------------------")
print(f"{hours_worked:<15.1f} {pay_rate:<10.2f} {overtime_hours:<10.1f} {overtime_pay:<15.2f} {regular_pay:<15.2f} {gross_pay:<15.2f}")

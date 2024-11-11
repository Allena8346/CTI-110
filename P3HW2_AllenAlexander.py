# Alexander Allen
#23Oct24
#P3HW2
#Calculate reg and OT pay for an employee

'''
Input: Get name from user as string
Input: Get number of hours worked worked as integer
Input: Get reg pay rate as float

Output a dotted line and the employee name

If the employee has OT (hours worked > 40.0)
calculate OT hours (hours worked - 40)
calculate OT pay rate (reg pay rate * 1.5)
calculate pay for reg hours(40 * reg pay rate)
calculate OT pay(OT hours * OT pay rate)
calculate gross pay(regpay + OT pay)


else (has no OT)
hours worked is the input value of hours worked
pay rate is the input value of pay rate
OT hours is 0
OT pay is 0
calculate pay for reg hours(40 * reg pay rate)
calculate gross pay(regpay + OT pay)

'''
name = input("Enter employee's name: ")
hoursWorked = int(input("Enter number of hours worked: "))
payRate = float(input("Enter employee's pay rate: "))

if hoursWorked > 40:
    OT = hoursWorked - 40
    OTpayRate = payRate * 1.5
    regPay = 40 * payRate
    OTpay = OT * OTpayRate
    grossPay = regPay + OTpay
else:
    OT = 0
    OTpayRate = payRate * 1.5
    regPay = hoursWorked * payRate
    OTpay = OT * OTpayRate
    grossPay = regPay + OTpay

print("-------------------------------------")
print("Employee name: ", name)
print()
print(f"{'Hours Worked':<15} {'Pay Rate':<10} {'OverTime':<10} {'OverTime Pay':<15} {'RegHour Pay':<15} {'Gross Pay':<15}")
print("---------------------------------------------------------")
print(f"{hoursWorked:<15.1f} {payRate:<10.1f} {OT:<10.1f} {OTpay:<15.2f} {regPay:<15.2f} {grossPay:<15.2f}")

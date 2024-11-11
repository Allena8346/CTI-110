# Alexander Allen
#06NOV24
#P4HW2
#Calculate reg and OT pay for multiple employees

name = input("Enter employee's" ' name or "Done"'" to terminate: ")
numEmploy = 0
OverPay = 0
normPay = 0
GrossPay = 0

while name.lower() != "done":
    hoursWorked = int(input(f"How many hours did {name} work? "))
    payRate = float(input(f"What is {name}'s pay rate? "))
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
#If Loop Break
    numEmploy += 1
    print("-------------------------------------")
    print("Employee name: ", name)
    print()
    print(f"{'Hours Worked':<15} {'Pay Rate':<10} {'OverTime':<10} {'OverTime Pay':<15} {'RegHour Pay':<15} {'Gross Pay':<15}")
    print("---------------------------------------------------------")
    print(f"{hoursWorked:<15.1f} {payRate:<10.1f} {OT:<10.1f} {OTpay:<15.2f} {regPay:<15.2f} {grossPay:<15.2f}")
    print()
    OverPay += OTpay
    normPay += regPay
    GrossPay += grossPay
    name = input("Enter employee's" ' name or "Done"'" to terminate: ")
    print()

#while Loop Break
print(f"Total number of employees entered: {numEmploy}")
print(f"Total amount paid for overtime: ${OverPay:,.2f}")
print(f"Total amount paid for regular hours: ${normPay:,.2f}")
print(f"Total amount paid in gross: ${GrossPay:,.2f}")


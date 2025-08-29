# House hunting Part A
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
r = 0.04

current_savings = 0.0
months = 0
target = total_cost * portion_down_payment

while current_savings < target:
    monthly_return = current_savings * r / 12
    monthly_salary = annual_salary / 12
    monthly_saved = monthly_salary * portion_saved

    current_savings += monthly_return + monthly_saved
    months += 1

print("Number of months:", months)

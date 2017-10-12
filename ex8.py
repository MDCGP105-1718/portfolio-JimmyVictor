annual_salary = float(input('What is your annual salary?: '))
portion_saved = float(input('How much of the salary are you saving?(as a decimal): '))
total_cost = float(input('How much does your dream home cost?: '))
semi_annual_raise = float(input('What is your semi annual raise? (as a decimal): '))
r = 0.04
monthly_salary = annual_salary / 12
current_savings = 0.0
portion_deposit = 0.20 * total_cost
number_of_months = 0
while current_savings < portion_deposit:
# looping until the current savings are bigger or equal to the portion deposit
    current_savings += monthly_salary * portion_saved
    current_savings += current_savings * r / 12
# calculating the new current savings each month
    number_of_months += 1
    if number_of_months % 6 == 0:
# checking if the number of months can be divided by 6
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary += annual_salary / 12
# calculating the new salary every 6 months

print('Number of months: ',number_of_months)

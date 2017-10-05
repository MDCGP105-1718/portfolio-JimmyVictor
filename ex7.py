annual_salary = float(input('What is your annual salary?: '))
portion_saved = float(input('How much of the salary are you saving?(as a decimal): '))
total_cost = float(input('How much does your dream home cost?: '))
r = 0.04
monthly_salary = annual_salary / 12
current_savings = 0.0
portion_deposit = 0.20 * total_cost
number_of_months = 0
while current_savings < portion_deposit:
    current_savings += current_savings * r / 12
    current_savings += monthly_salary * portion_saved
    number_of_months += 1

print('Number of months: ',number_of_months)

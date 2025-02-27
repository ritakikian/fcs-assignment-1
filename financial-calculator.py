#ask for financial details
salary = float(input("what is your salary? "))
month_name = input("what is the month you want to store your salary for? ")
savings = float(input("enter percentage of your savings: "))
rent = float(input("enter percentage of your rent: "))
electricity = float(input("enter percentage of electricity: "))

#print the financial details
print("your salary for the month of ", month_name, " is: ", salary)
allocated_savings = salary * savings / 100
print("your savings for the month of ", month_name, " is: ", allocated_savings)
allocated_rent = salary * rent / 100
print("your rent for the month of ", month_name, " is: ", allocated_rent)
allocated_electricity = salary * electricity / 100
print("your electricity for the month of ", month_name, " is: ", allocated_electricity)

#calculate the total expenses
total_expenses = (allocated_savings) + (allocated_rent) + (allocated_electricity)
print ("your total expenses for the month of ", month_name, " is: ", total_expenses)

#calculate the remainder after expenses
remainder = salary - total_expenses
print("your remainder for the month of ", month_name, " is: ", remainder)

#calculate yearly expenses on rent and electricity
yearly_rent = 12 * (allocated_rent)
yearly_electricity = 12 * (allocated_electricity)
print("your total yearly expenses on rent and electricity: ", yearly_rent + yearly_electricity)

#calculate salary ^2
salary_squared = salary ** 2
print("your salary squared is: ", salary_squared)

#calculate total savings
additional_savings = float(input("enter additional savings: "))
total_savings = (allocated_savings) + additional_savings 

if total_savings > 0:  
    remaining_amount = (additional_savings / total_savings) * 100 
else:
    remaining_amount = 0  

#print total savings and remaining amount
print("your total savings (including additional savings): ", total_savings)
print("remaining amount as percentage of total savings: ", remaining_amount, "%")
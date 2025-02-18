#ask for financial details
salary = float(input("what is your salary? "))
month_name = input("what is the month you want to store your salary for? ")
savings = float(input("enter percentage of your savings: "))
rent = float(input("enter percentage of your rent: "))
electricity = float(input("enter percentage of electricity: "))

#print the financial details
print("your salary for the month of ", month_name, " is: ", salary)
print("your savings for the month of ", month_name, " is: ", salary * savings / 100)
print("your rent for the month of ", month_name, " is: ", salary * rent / 100)
print("your electricity for the month of ", month_name, " is: ", salary * electricity / 100)

#calculate the total expenses
total_expenses = (salary * savings / 100) + (salary * rent / 100) + (salary * electricity / 100)
print ("your total expenses for the month of ", month_name, " is: ", total_expenses)

#calculate the remainder after expenses
remainder = salary - total_expenses
print("your remainder for the month of ", month_name, " is: ", remainder)

#calculate yearly expenses on rent and electricity
yearly_rent = 12 * (salary * rent / 100)
yearly_electricity = 12 * (salary * electricity / 100)
print("your total yearly expenses on rent and electricity: ", yearly_rent + yearly_electricity)

#calculate salary ^2
salay_squared = salary ** 2
print("your salary squared is: ", salay_squared)


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
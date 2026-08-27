#Input for trip expense tracker
ticket = int(input("Enter the cost of train/bus ticket: "))
taxi_fare = int(input("Enter the cost of taxi fare: "))
stay_rent = int(input("Enter the cost of stay rent: "))
groceries = int(input("Enter the cost of grocerries purchased: "))
miss_expenses = int(input("Enter the cost of other misselenious expenses: "))
#To calculate total expense
total = ticket + taxi_fare + stay_rent + groceries + miss_expenses
#Table chart
print("----------------------------------------")
print("\tExpenses details")
print("----------------------------------------")
print("Ticket         :",ticket)
print("Taxi Fare      :",taxi_fare)
print("Stay Rent      :",stay_rent)
print("Groceries      :",groceries)
print("Other expenses  :",miss_expenses)
print("----------------------------------------")
print("Total          :",total)
print("----------------------------------------")
print()
#To calculate per person share in the expense
people = int(input("Enter the number of pepole on the trip: "))
per_person = total/people
print("The per person share in the expense is: ",per_person)
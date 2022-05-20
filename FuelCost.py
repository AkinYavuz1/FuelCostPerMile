from fileinput import close

print("How much did you pay for your Pence per litre?")
fuel_cost = (float(input()))

print("input your miles travelled: ") 
miles = int(input())

print("What is your average MPG?")
mpg = int(input())

miles_per_litre = mpg / 4.546

cost_of_journey = round((miles * fuel_cost) / miles_per_litre,2)
cost_per_mile = round(cost_of_journey  / miles,2)

print(f'The cost for the journey is: £{cost_of_journey}')
print(f'The cost per mile is: £{cost_per_mile}')

input("Press Enter to close.")
#collect input from user
#collect input for the distance
#collect input for price per gallon
#compute the three to get the cost of driving 
#print the cost of driving
distance = int(input("Enter distance"))

miles_per_gallon = int(input("Enter miles per gallon"))

price_per_gallon = int(input("Enter price per gallon"))

total_cost_of_driving = distance / (price_per_gallon * miles_per_gallon)

print("The cost of driving is:", total_cost_of_driving)

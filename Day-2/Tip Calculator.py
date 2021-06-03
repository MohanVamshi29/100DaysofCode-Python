
print("Welcome to the tip calculator")
bill=float(input("What was the total bill $ ? \n"))
percentage=int(input("what percentage tip would you like to give? 10 , 12 ,15 ...?\n"))
number_of_people=int(input("how many people are splitting the bill ? \n"))
total= percentage/100 * bill + bill
split=total/number_of_people
print(f"Each person should pay: ${round(split,2)}")


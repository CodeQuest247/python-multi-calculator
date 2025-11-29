# PA2, CS 7, Section D01, 9/12/2024, Aditi Menon
#Section 1 calculates the cost per mile of gas.
#It first asks the user to enter the cost of the tank of gas and the number of miles driven.
gasCost = float(input("Enter the cost of the tank of gas:\n"))
milesDriven = float(input("Enter the number of miles driven:\n"))
#Then it calculates the cost of gas per mile driven by dividing the cost of the tank of gas by the number of miles driven.
cost_per_mile = gasCost / milesDriven
#After calculating the cost per mile of gas, it prints the cost of the tank of gas and the number of miles driven that the user put in.
print(f"Cost of gas:                  ${gasCost:10.2f}")
print(f"Miles driven:                  {milesDriven:10.2f}")
#And in the end it prints the actual cost per mile.
print(f"Cost per mile:                ${cost_per_mile:10.2f}")

#Section 2: Calculating annual and daily compounded interest rate
principalAmount = float(input("Enter the principal amount:\n"))
interestRate = float(input("Enter the interest rate:\n"))
#Convert annual interest rate percentage into a decimal
decimal_rate = interestRate / 100
#Calculation for the interest earned during one year, compounded annually: interest earned = starting principal * interest rate
interest_compounded_annually = principalAmount * decimal_rate
#Find total amount annual amount by adding the principal to the interest compounded annually
# Print statements including the principal amount, annual rate, and total amount for annually compounded interest rate
total_annual_amount = principalAmount + interest_compounded_annually
print(f"For a loan of                ${principalAmount:10.2f}")
print(f"with a rate of               ${interestRate:10.2f} %")
print(f"interest compounded annually ${interest_compounded_annually:10.2f}")
print(f"YE balance                   ${total_annual_amount:10.2f}")
#Now find the interest compounded daily amount
interest_compounded_daily = principalAmount * ((1 + (decimal_rate/365))**365) - principalAmount
#After finding the daily compounded amount, add that number to the starting principal to find out the total
#Then, print the daily compounded amount and the total amount
total_daily_amount = principalAmount + interest_compounded_daily
print(f"interest compounded daily    ${interest_compounded_daily:10.2f}")
print(f"YE balance                   ${total_daily_amount:10.2f}")

#Section 3 calculates the diagonal measurement of your screen in inches
#Asks user for the height and width of the screen and creates a variable for each
height = float(input("Enter the height of your display screen in inches:\n"))
width = float(input("Enter the width of your display screen in inches:\n"))
#First, import math. Then, using the two variables the diagonal length of the screen is calculated using the Pythagorean Theorem.
import math
diagonal = math.sqrt((height**2) + (width**2))
#Then, the diagonal length of the screen in inches is printed
print(f"The diagonal size of the screen is {diagonal:.2f} inches.")


import math

#This program calculates interest on an investment or a property bond. 

print(" investment - to calculate the amount of interest you'll earn on your investment\n bond       - to calculate the amount you'll have to pay on a home loan")

#User selects which calculation they would like to program to perform.
selection = input("Enter either 'investment' or 'bond' from the menu above to proceed:\n")
selection = selection.lower()

#User inputs loan details as numerical variables. 
if selection == "investment":
    deposit = float(input("How much money are you depositing?\n"))
    rate = float(input("What is the percentage interest rate?\n"))
    term = int(input("How many years do you plan to invest for?\n"))
    interest = input("Is the interest 'simple' or 'compound'?\n")
    interest = interest.lower()
    interest_2 = float(rate / 100)

    # The program will apply the relevant formula to calculate the interest.
    #Total interest amounts are cobverted to two decimal places.
    if interest == "simple":
        total_amount = deposit *(1 + interest_2*term)
        print(f"The total amount you will earn on your investment is {round(total_amount, 2)}")
    else:
        total_amount = deposit * math.pow((1+interest_2), term)
        print(f"The total amount you will earn on your investment is {round(total_amount, 2)}")

#User inputs property details. 
#The program calculates the total interest to be paid each month.
elif selection == "bond":
    house_value = int(input("What is the current value of the property?\n"))
    rate = float(input("What is the percentage interest rate?\n"))
    term = int(input("How many months will you take to repay the bond?\n"))
    monthly_rate = (rate / 100) / 12
    total_amount = (monthly_rate * house_value)/(1 - (1 + monthly_rate)**(-term))
    print(f"The total amount you will repay each month is {round(total_amount, 2)}.")

#If the original input is not either 'investment' or 'bond' an error message will print.
else:
    print("You have entered an invalid selection.")

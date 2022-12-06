import math

print("""
Choose either 'investment' or 'bond' to proceed 

investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
""")
calculation = input("Enter the calculation type: ").upper()

# If user chosen 'investment'
# Ask the user to enter amount, interest rate, number of years and type of interest
# Calculate the amount he will receive after N years based on entered information

if calculation == "INVESTMENT":
    amount = float(input("Enter the amount of money your are depositing: "))
    interest_rate = float(input("Enter the interest rate (number without percent): ")) / 100
    years = int(input("Enter the number of years you plan on investing: "))
    interest = input("Choose interest type (Simple or Compound): ").upper()

    if interest == "SIMPLE":
        result = math.ceil(amount * (1 + interest_rate * years))
        print(f"The amount you will be given back after {years} years = R{result}")

    elif interest == "COMPOUND":
        result = math.ceil(amount * (1 + interest_rate) ** years)
        print(f"The amount you will be given back after {years} years = R{result}")

# If user chosen 'bond'
# Ask the user to enter present house value, interest rate and number of months
# Calculate the amount he will have to pay each month based on entered information

elif calculation == "BOND":
    house_value = float(input("Enter the present value of your house: "))
    interest_rate = float(input("Enter the interest rate (number without percent): ")) / 100 * (1 / 12)
    months = float(input("Enter the number of months you plan to take repay the bond: "))

    result = math.ceil((interest_rate * house_value) / (1 - (1 + interest_rate) ** (-months)))
    print(f"The amount you will have to repay each month = R{result}")

# If the user didn't type in a valid input, show error message:
else:
    print("Choose a valid entry")

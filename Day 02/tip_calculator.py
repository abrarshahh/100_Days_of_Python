print("!! Welcome to the tip calculator !!")
bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10 12 or 15? ")
people = input("How many people are splitting the bill? ")

n_bill = float(bill)
n_tip = float(tip)
n_people = int(people)

n_tip /= 100
n_bill = n_bill + (n_bill * n_tip)

total = round(n_bill / n_people , 2)
print(f"Each person should pay ${total}.")
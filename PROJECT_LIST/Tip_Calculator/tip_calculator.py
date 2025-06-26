print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_as_person = tip / 100
total_tip_amount = bill * tip_as_person
total_bill = bill + total_tip_amount
bil_per_persons = total_bill / people

final_amount = round(bil_per_persons,2)
print(final_amount)
print(f"Each person should pay : {final_amount}")

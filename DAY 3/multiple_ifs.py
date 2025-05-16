print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("child ticket $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket $7.")
    else:
        bill = 12
        print("Adult ticket $12.")
    choice = input("Do you want to photo take ? Type y for yes and N for No. ")
    if choice == "y":
        #add $3
        # photo_bill = 3
        # total_bill = bill+photo_bill
        # bill = bill+3
        bill += 3
        print(f"Your total bill is {bill}")
    else:
        print(f"Your total bill is : {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")

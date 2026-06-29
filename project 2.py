print("Welcome to TIP CALCULATOR ")
bill=float(input("what was the total bill ? "))
tip=int(input("what prcentage tip would you like to give ? 10, 12, 15"))
people=int(input("how many people to spilt the bill ? "))
bill_with_tip= tip/10 *bill + bill
print(bill_with_tip)
bill_per_person= (bill_with_tip)/people
final_amount=round(bill_per_person, 2)             #round off
print(f"each person should pay {final_amount}")    #fstring


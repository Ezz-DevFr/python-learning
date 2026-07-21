age = int(input("what is your age "))
has_ticket = input("do you have a ticket? ")
if age >= 18 and has_ticket == "yes":
    print("welcome!")
else:
    print("access denied")
print("Welcome to PizzaHub please make an order")
size = input("What size bill do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your bill? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill = 15

elif size == "M":
    bill = 20
    
elif size == "L":
    bill = 25

else:
    print("Please enter a valid input ")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"The total bill is ${bill} ")
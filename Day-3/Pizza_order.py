"""
Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small pizza (S): $15

Medium pizza (M): $20

Large pizza (L): $25

Add pepperoni for small pizza (Y or N): +$2

Add pepperoni for medium or large pizza (Y or N): +$3

Add extra cheese for any size pizza (Y or N): +$1

Example Input
L
Y
N
Example Output
Thank you for choosing Python Pizza Deliveries!
Your final bill is: $28.
"""

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N\n") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N\n") # Do you want extra cheese? Y or N

#initializing bill
bill = 0;

if size == 'S':
#added the amout for choosing small pizza
    bill += 15;
    if add_pepperoni == 'Y':
        bill += 2;
        if extra_cheese == 'Y':
            bill =+ 1;
elif size == 'M' or "L":
    if size == 'M':
        bill += 20;
    else:
        bill += 25;
    
    if add_pepperoni == 'Y':
        bill += 3;

if extra_cheese == 'Y':
    bill += 1;
    
print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}.");
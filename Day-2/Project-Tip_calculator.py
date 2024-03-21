#print welcome message.
print("Welcome to the tip calculator!");

#get the total bill form the user.
total_bill=float(input("What was the total bill?\n"));

#get the persentage of tip you like to give.
tip_percent = int(input("How much tip would you like to give?\ntip percentage- 10, 12, or 15?\n"));

#here we get the tip amount
tip_amt = total_bill * (tip_percent/100);

#get how many people to split the bill with.
total_people = int(input("How many people to split the bill?\n"));

#calculate each person share.
each_person_share = round((total_bill + tip_amt) / total_people, 2);

print("Each person should pay:"+ " " + f"{each_person_share}" );
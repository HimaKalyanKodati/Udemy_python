#In this excersice you will learn
#1.Type casting.
#2.Mathematical operations.

#BMI formula BMI = weight(kg)/height^2 (m^2).
#Taking input height in meters and conver it into float(casting the variable to float).
height=float(input("What is your height? In meters.\n"));

#Taking input weight in meters.
weight=float(input("Please enter weight? In kg's.\n"));

#calculate BMI.
#for this code no rounding is needed.
#BMI=round((weight/(height**2)),2);

BMI=(weight/(height**2));
      
#Below code is pending.
#Here we need to write the code to print message based on BMI chart, Need to satisfy the conditions below.
"""
Under 18.5 they are underweight
Equal to or over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.

"""

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI >= 18.5 and BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI >= 25 and BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI >= 30 and BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
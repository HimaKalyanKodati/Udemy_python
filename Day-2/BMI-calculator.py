#In this excersice you will learn
#1.Type casting.
#2.Mathematical operations.

#BMI formula BMI = weight(kg)/height^2 (m^2).
#Taking input height in meters and conver it into float(casting the variable to float).
height=float(input("What is your height? In meters.\n"));

#Taking input weight in meters.
weight=float(input("Please enter weight? In kg's.\n"));

#calculate BMI.
BMI=str(weight/height**2);

print("Your BMI is" + " " + BMI);
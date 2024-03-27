#Please enter the year to check wheather the year is leap year or not.
year = int(input("Enter the year to check.\n"));

#Here need to satisfy the below contion to check wheathrt the year is leap year or not.

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print (f"The given year {year} is leap year.")
    else:
        print (f"The given year {year} is not a leap year.")
else:
    print(f"The given year {year} is not a leap year.")
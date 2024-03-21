#In this we can learn.
#1.f-strings.
#f-sting is used to concatinate integer or floats to strings.

#Take age as input.
age=int(input("What is your current age?\n"));

#calculate the year remaining before turning 90.
years_rem= 90 - age;

#calculate the weeks remaining. For year there are 52 weeks.
weeks_rem = years_rem * 52;

#calculate the number of days. For year there are 365 days (don't consider leap year for now).
days_rem = years_rem * 365;

#print the output in using f-string.
print(f"You have {years_rem} years, {weeks_rem} weeks and {days_rem} days remaing before turning into 90.");

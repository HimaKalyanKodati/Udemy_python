# Input a Python list of student heights
#This will store the input values as string
student_heights = input().split()
#converting the input strings into intigers
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above
  
# Write your code below this row

#use sum funtion in python and sum the total and store it in one variable.
#rule, To finish the exercise suing one for loop. 

# total_height = int(sum(student_heights));
total_height = 0
for count in student_heights:
    total_height = int(total_height + count);

#get the total numbers
total_numbers = int(len(student_heights));


#calculate the average height and rounded to remove the decimal value.
average_height = round((total_height/total_numbers));

print(f"total height = {total_height}");
print(f"number of students = {total_numbers}");
print(f"average height = {average_height}");
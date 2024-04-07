# Input a list of student scores
#This will store the input values as string
student_scores = input().split()
#converting the input strings into intigers
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row

#initialise the high_score with zero and write one for loop for storing the high score
high_score = 0;

for score in student_scores:
    if high_score < score:
        high_score = score


#print the high score
print(f"The highest score in the class is: {high_score}")
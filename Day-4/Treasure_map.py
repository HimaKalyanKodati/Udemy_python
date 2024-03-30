line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

#code for index1 or we can use index() function.
if position[0] == "A":
    index1 = 0;
elif position[0] == "B":
    index1 = 1;
else:
    index1 = 2;
    
#code for index2
if position[1] == "1":
    index2 = 0;
elif position[1] == "2":
    index2 = 1;
else:
    index2 = 2;
    


map[index1][index2] = 'X'

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
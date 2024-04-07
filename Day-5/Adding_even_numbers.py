target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here

#Here I am initializing one variable with zero and write the loop with range funtion.

total_even_numbers = 0;

for count in range(0,target+1):
    if count % 2 == 0:
        total_even_numbers += count;

print(total_even_numbers);
print("The Love Calculator is calculating your score...")
name1 = input("Input name1\n") # What is your name?
name2 = input("Input name1\n") # What is their name?

#combine the letters.
combine_name = name1 + name2;

#convert all the input in to lower case using lower() function.
combine_name = combine_name.lower();

#get individual count using count() function.

t = combine_name.count("t");

r = combine_name.count("r"); 

u = combine_name.count("u");

e = combine_name.count("e");



l = combine_name.count("l");

o = combine_name.count("o");

v = combine_name.count("v");

e = combine_name.count("e");

#add the true and love count seperatly.
first_word = str(t + r + u + e);

second_word = str(l + o + v + e);

#combine two words to get the love score.
score = int(first_word + second_word);

#evaluate the condtion based on the score we get.
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.");
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.");
else:
    print(f"Your score is {score}.")
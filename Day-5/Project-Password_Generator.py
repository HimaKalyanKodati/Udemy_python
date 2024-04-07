#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Here I am initializing empty list and using the loops with range funtion
#loop for random letters.
tot_letters = [];
for count in range(0,nr_letters):
    tot_letters.append(random.choice(letters));
    
#loop for symbols
tot_symbols = [];
for count in range(0,nr_symbols):
    tot_symbols.append(random.choice(symbols));

#loop for numbers
tot_numbers = [];
for count in range(0,nr_numbers):
    tot_numbers.append(random.choice(numbers));


tot_password = (tot_letters + tot_symbols + tot_numbers);


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91    

gen_password = ''
for count in range(0,len(tot_password)):
    gen_password += tot_password[count];


#print the generated password
print("Here is your password: " + gen_password);


#===============================================================#
#===============================================================#
#===============================================================#


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

tot_shuffle_password = tot_password
random.shuffle(tot_shuffle_password);

hard_password = '';
for count in range(0,len(tot_shuffle_password)):
    hard_password += tot_shuffle_password[count];


#print the generated password
print("Here is your password: " + hard_password);
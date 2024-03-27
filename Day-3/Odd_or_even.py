#Check input in number is odd or even.

#get input number.
number = int(input("Enter input number?\n"));

#get modulus of the number(modules- %).
check_num = number % 2;

#check wheather it is even or odd number.
#if it is even number the modulus returns '0'.
#if it is odd number the modulus returns non-zero.

if check_num == 0:
    print(f"Given numeber {number} is even number.")
else:
    print(f"Given numeber {number} is odd number.")
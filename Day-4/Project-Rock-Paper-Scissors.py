#import random module.
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 

#list of items stored in list.
hands = [rock, paper, scissors];

#take user input.
my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"));

#print the user choise output.
print(hands[my_choice]);

#here chose the random output for the computer.
computer_choice = random.randint(0,2);

#print computer output.
print("Computer chose:\n" + hands[computer_choice]);


#conditions or rules check to win the game.
if my_choice < computer_choice:
    print("You lose");
elif my_choice == 2 and computer_choice == 0:
    print("You lose");
elif my_choice == computer_choice:
    print("You draw");
else:
    print("You win");
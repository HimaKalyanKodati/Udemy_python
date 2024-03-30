#import random
import random

#use split command to take all the inputs. split().
names = input("What are the names?\n").split(", ");

#use choice in random module.
payer = random.choice(names);

print(payer + " is going to buy the meal today!");
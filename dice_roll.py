import random
import time

print("Let's roll the dice!")
time.sleep(1)

#minimum and maximum number on dice
die_min = 1
die_max = 6

#User input
start = input("Are you ready to roll?: Y/N ")

while start.upper() != 'N':

    if start.upper() == 'Y':

        print("Rolling Dice...")
        time.sleep(1)
        print(random.randint(die_min,die_max))
        print(random.randint(die_min,die_max))

        start = input('Would you like to roll again?: Y/N ')

    else:

        start = input('Please enter Y/N: ')
        
print('See you later!')




        
    




                    


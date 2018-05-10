"""
===================   TASK 2   ====================
* Name: Roll The Dice
*
* Write a script that will simulate rolling the
* dice. The script should fetch the number of times
* the dice should be "rolled" as user input.
* At the end, the script should print how many times
* each number appeared (1 - 6).
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""


# Write your
from random import randint

import random
strana1=0
strana2=0
strana3=0
strana4=0
strana5=0
strana6=0
for i in range(1000):

    pala=random.randint(1,6)

    if pala==1:

        strana1 +=1
    elif pala==2:
        strana2 +=1
    elif pala==3:
        strana3 +=1
    elif pala==4:
        strana4 +=1
    elif pala==5:
        strana5 +=1
    elif pala==6:
        strana6 +=1


print("Pala strana1: " + str(strana1))
print("Pala strana2: " + str(strana2))
print("Pala strana3: " + str(strana3))
print("Pala strana4: " + str(strana4))
print("Pala strana5: " + str(strana5))
print("Pala strana6: " + str(strana6))
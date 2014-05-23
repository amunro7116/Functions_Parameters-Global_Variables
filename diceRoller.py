#Die roll task
import random,time
d1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
d2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
d3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
d4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
d5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
d6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

def rollDice():
    print("rolling.....")
    time.sleep(0.5)
    roll = random.randint(1,6)
    return roll

def showDice(roll):
    if roll == 1:
        print(d1)
    elif roll == 2:
        print(d2)
    elif roll == 3:
        print(d3)
    elif roll == 4:
        print(d4)
    elif roll == 5:
        print(d5)
    else:
        print(d6)

roll=rollDice()
showDice(roll)
#This program uses if staements and functions and variables to execute the task
#This i believe is the most efficient way of doing the set task.
#Enjoy :)

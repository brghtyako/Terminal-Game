import os
import time
import random
import sys

def restart_program():   

    python = sys.executable
    os.execl(python, python, * sys.argv)

#Created a code to restart our script

damage = 0
defence = 0
Umove = 0
Bmove = 0

print("Welcome to the terminal based game! Created by Brghtyako. Enjoy!")
time.sleep(2)
print("Hi player! You need to choose a profession to begin the adventure. There are 3 professions that you can choose.")
time.sleep(3)
print("First profession is Swordmanship. Swordmans has 20 damage points and 10 defence points.")
time.sleep(4)
print("Second one is Archery. Archers has 15 damage points and 15 defence points.")
time.sleep(4)
print("And the last one is Magic. Magicians has 10 damage points and 20 defence points.")
time.sleep(4)
print("Warning! Once you select your profession, you can't change it during the game.")
time.sleep(4)
print("About battle system: when you select your move, AI selects a move too; who has more points on that category wins. If it is tie, AI wins.")
time.sleep(8)

profession = input("Select your profession. Press 1 for swordmanship, 2 for archery and 3 for magic: ")

if profession == "1":
    damage + 20
    defence + 10
elif profession == "2":
    damage + 15
    defence + 15
elif profession == "3":
    damage + 10
    defence + 20

if profession == "1":
    print("Good choice. Now you are a swordman")
    time.sleep(4)

elif profession == "2":
    print("Good choice. Now you are an archer")
    time.sleep(4)

elif profession == "3":
    print("Good choice. Now you are are a magician")
    time.sleep(4)

print("Get ready. Now it's time to fight the first monster. It called BreadG. It can damage 15, his defence point is 20.")
time.sleep(10)

move = input("What are you gonna do? Press 0 for attack, 1 for defence: ")

if move == "0":
    Umove = random.randint(0, int(damage))
if move == "1":
    Umove = random.randint(0, int(defence))

BreadGmove = random.randrange(2)

if BreadGmove == "0":
    Bmove = random.randrange(15)
if BreadGmove == "1":
    Bmove = random.randrange(20)

if Umove >= Bmove:
    print("Congragulations! You defeated first monster.")

else:
    play = input("Oh no! Monster killed you. Wanna try again? (y/n): ")
    if play == "y":

        restart_program()
    
    if play == "n":
        
        sys.exit()



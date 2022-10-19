from ast import Pass
import math
from operator import truediv
import os
import time
import random as rand
import sys

damage = 0
defence = 0
Umove = 0
Bmove = 0

texts =	{
    'Welcome to the terminal based game! Created by Brghtyako. Enjoy!':2,
    'Hi player! You need to choose a profession to begin the adventure. There are 3 professions that you can choose.':3,
    'First profession is Swordmanship. Swordmans has 20 damage points and 10 defence points.':4,
    'Second one is Archery. Archers has 15 damage points and 15 defence points.':4,
    'And the last one is Magic. Magicians has 10 damage points and 20 defence points.':4,
    'Warning! Once you select your profession, you can\'t change it during the game.':4,
    'About battle system: when you select your move, AI selects a move too; who has more points on that category wins.\n If it is tie, AI wins.':8

}

monsterNames = ['BreadG','Boss2','Boss3']


def setValues():
    damage = 0
    defence = 0
    Umove = 0
    Bmove = 0

def start(fast):
    setValues()
    currentBoss=0
    for text, sleepTime in texts.items():
        print(text,'\n')
        if(not fast) :
            time.sleep(sleepTime)
    pass

    profession = input("Select your profession. Press 1 for swordmanship, 2 for archery and 3 for magic: ")
    global damage
    global defence
    if profession == "1":
        
        damage += 20
        defence += 10
        print("Good choice. Now you are a swordman")
    elif profession == "2":
        damage += 15
        defence += 15
        print("Good choice. Now you are an archer")
    elif profession == "3":
        damage += 10
        defence += 20
        print("Good choice. Now you are are a mage")
    time.sleep(4)
      
    global monsterNames
    while True:
        result=play(monsterNames[currentBoss],(currentBoss+1)*rand.randint(10,20),(currentBoss+1)*rand.randint(10,20),(currentBoss+1)*rand.randint(50,200))
        if result:
            b=input('You defeated {name}, type any thing to continue type \"exit\" to exit' ).lower()

            if b=='exit':
                break
            currentBoss+=1

            if currentBoss>=len(monsterNames):
                currentBoss=0
        else:   
            b=input('You lost {name}(rip bozo), press a key to restart type \"exit\" to exit'.format(name=monsterNames[currentBoss]) ).lower()

            if b=='exit':
                break
            start(True)
    sys.exit()      




def calculateDamage(dmg,dd):
    return (max(dmg,dd+1)-dd)*5
def play(name,bossDef,bossAtt,bossHp):

    print("Get ready. Now it's time to fight with the monster. It called {bossName}. It can attack damage is {att}, his defence point is {dd} and his hp is {hp}.".format(bossName=name,att=bossAtt,dd=bossDef,hp=bossHp))
    time.sleep(6)
    localHp=bossHp
    hp=100
    turn=0
    defBoost1=0
    defBoost2=0

    while localHp>0 and hp>0:
        if turn==0:
            i=str(input('Type 1 to attack or type 2 to defend: \n'))

            if i=='1':
                global damage
                dmg=calculateDamage(damage,bossDef)
                print('You dealt {damage} damage to the boss'.format(damage=dmg))
                localHp-=max(max(dmg,1)/max((defBoost1*2),1),1)
                defBoost2=0
            else:
                #failsafe
                print('You are preparing for {name}\'s attack'.format(name=name))
                defBoost1=1;
            turn=1
            time.sleep(2)
            continue
        turn=0
        if rand.randint(0,1)==0:
            global defence
            dmg=calculateDamage(bossAtt,defence)
            print('{name} dealt {damage} damage to you'.format(name=name,damage=dmg))
            hp-=max(max(dmg,1)/max((defBoost1*2),1),1)
            defBoost1=0
        elif defBoost1==1:
            print('You both defended yourself, skipping...')
            defBoost1=0
            defBoost2=0
        else: 
            print('{name} is preparing for your next attack'.format(name=name))
            defBoost2=1
        time.sleep(2)    
    if localHp<=0:
        return True
    return False

    
if __name__ == '__main__' :
    start(True)


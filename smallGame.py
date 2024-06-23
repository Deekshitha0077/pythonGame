#Random number game
import random
import time
print("-------Welcome to the game------")
time.sleep(1)
print("-------START-------")
time.sleep(1)
count1=0
count2=0
for i in range(1,6):
    print('PLAYER A\'s TURN')
    num1=int(input('Enter a number from 1-1000\n'))
    time.sleep(1)
    print(num1)
    count1=count1+num1
    time.sleep(1)
    print('PLAYER B\'s TURN')
    num2=random.randint(0,1001)
    time.sleep(1)
    print(num2)
    count2=count2+num2
time.sleep(1)
print('PLAYER A SCORE:',count1)
print('PLAYER B SCORE:',count2)
time.sleep(1)
if(count1==count2):
    print("-----TIE-----")
elif(count1>count2):
    print("-----PLAYER A IS THE WINNER-----")
else:
    print("-----PLAYER B IS THE WINNER-----")
print("-----GAME OVER-----")
    
    
    

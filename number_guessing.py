# Number Guessing Game
import random
x=0
num=int(input('guess the number between 1 and 100 choosen by the computer:'))
computer_sel_num=random.randint(1,100)
while x<2:
  if num==computer_sel_num:
     print('congratulations you won the game!!!')
     break
  elif num>computer_sel_num:
     print("you've guessed Too high")
     num=int(input('Try again:'))
     x+=1
     if x==2 and num!=computer_sel_num:
        print("you've lost the game (*_*)")
  elif num<computer_sel_num:
     print("you've guessed too low")
     num=int(input('Try again:'))
     x+=1
     if x==2 and num!=computer_sel_num:
        print("you've lost the game (*_*)")
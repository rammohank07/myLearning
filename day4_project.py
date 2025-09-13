##Developing the mini project using the python basics
print('Guessing the secret number')
'''
s_n=89
n=int(input('Enter the number to find the secret code:  '))
while n!=s_n:
    if  s_n-5 <n< s_n+5:
        print('Your guessing number is near to the secret code ')
    else:
        print('Your guessing number is far to the secret code ')
    t=str(input('Do you want to try again Y or N  :  '))
    if t=='N':
        print ('Thanks for playing the game')
        break
    else:
        n = int(input('Enter the number to find the secret code:  '))
if n==s_n:
    print('Congratulations! your guess is correct and the secret number is: ',s_n)
'''
import random
s=random.randint(65,95) #secret number between 65 and 95
attempts=5
while attempts>0:
    n=int(input('Enter the number to find the secret code(65-95)  :  '))
    if n==s:
        print(f" Congratulations your guess is correct and the secret number is: {s} ")
        break
    elif abs(s-n)<=5 and attempts>0:
        n1=input(" Your guess is near to  the secret number , Press N to exit else press any key to continue?  ")
        if n1.upper()=='N':
            break

    elif n<s and attempts>0:
        n1=input('Too low , Press N to exit else press any key to continue ')
        if n1.upper()=='N':
            break
    elif n>5 and attempts>0:
        n1=input('Too high , Press N to exit else press any key to continue ')
        if n1.upper()=='N':
            break
    attempts-=1
    if attempts==0:
        print(f" Sorry , you are out of attempts! the secret number is {s}")

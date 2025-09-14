
#Practicing modules
import math
import random
import datetime

print ("Square root of 81 is", math.sqrt(81),' ,',round(math.sqrt(89),2))
print("pi value is",round(math.pi,2))
print(" 3 power of 5 is: ",math.pow(3,5))
print(" 10 log 100 is : ",math.log(10,100))
print("Ceil value : ", math.ceil(-5.2))
print("floor value : ", math.floor(-5.2))
#print (3**5)
#print((lambda n: n**5)(3))
print(f'Factorial of 5 is {math.factorial(5)}')
# Accessing functions from  random module
print(" Fetching random number berween 20 to 50 and the number is ",random.randint(20,50))
print("selecting the choice from list", random.choice(['America','India','China','Russa']))
#Practicing date time module
print("Curent date :  ",datetime.date.today())
print("Current time:  ",datetime.datetime.now().strftime('%H:%M:%S'))
## Challange
n=float(input("Enter the number :  "))
print (f"factorial of number is {math.factorial(round(n))}")
print (f"squareroot of number is {math.sqrt(n)}")
print (f"floor of number is {math.floor(n)}")
print (f"ceil of number is {math.ceil(n)}")

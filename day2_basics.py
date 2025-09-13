## Day 2 practice ##
######Arthmetic Operators
num1=int(input('Enter the value for first number'))
num2=int(input('Enter the value for second value'))
#Addition
print('Sum of two given numbers ', num1+num2)
#Substraction
print('Difference of two given numbers ', num1-num2)
#multiplication
print('Multiplication of two given numbers ', num1*num2)
#Division
print('Division of two given numbers ', num1/num2)
#Floor Division
print('Floor Division  of two given numbers ', num1//num2)
#Module
print('Module of two given numbers ', num1%num2)
#Power
print('Power of two given numbers ', num1**num2)

###Comparision Operators

print('comparision operators')
#num1=int(input('Enter the value for first number'))
#num2=int(input('Enter the value for second value'))
print('num1==num2: ',num1==num2)
print('num1!=num2: ',num1!=num2)
print('num1>num2: ',num1>num2)
print('num1<num2: ',num1<num2)
print('num1>=num2: ',num1>=num2)
print('num1<=num2: ',num1<=num2)
### Conditional OPerators

print('Verifying given number is even or odd')
#num1=int(input('Please Enter the number'))
if num1%2==0:
    print('Given number ',num1,' is Even number')
else:
    print('Given number ', num1, ' is Odd number')
print('Pass or Fail based on marks')
marks=int(input('Please Enter the marks'))
if marks>=35:
    print('You are passed and your marks are ',marks)
else:
    print('You are Failed and your marks are ', marks)
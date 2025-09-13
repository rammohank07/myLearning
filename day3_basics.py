### Python Day 3 practice

# while loop
print('practicing while loop')
i=0
while i<6:
    print ('The number is ',i)
    i=i+1

## For loop
print ('practicing for loop')
for i in range(2,8):
    print('The number is  ',i)

## Break and continue
print(' Break and  continue example')
for i in range(1,8):
    if i==2:
        continue # Skip number 2
    if i==6:
        break # stop loop when i=6
    print ('The number is ',i)

##Print table
print('table printing of given number ')
num=int(input('Enter the number for the table printing: '))
for i in range(1,11):
    print(num,'*',i,'=',num*i)

print('Printing the sum of number up to given number ')
num=int(input('Enter the number for the sum printing: '))
total=0
expr=''
for i in range(1,num+1):
    total+=i
    expr+=str(i)
    if i<num:
        expr+="+"
    else:
        expr+= "="+ str(total)
print('-->',expr)
###Triangle Patern
print('Triangle pattern')
n=5
for i in range(1,n+1):
    #print(' '*(n-1)+"*"*i)
     print('    ','*'*i)

## Day 4 practice
print("Printing the natural numbers")
for i in range(0,11):
    print(i,end=' ')
print('')
print("Characters from the words")
for i in 'PYTHION':
    print(i,end=' ')
print('')
print('Even numbers between 1 to 20')
for i in range(1,21):
    if i%2==0:
        print(i, end=' ')
print('')
print('Words from list')
l=['apple','banana','orange','sapota','cherry']
for i in l:
    print (i,end=' ')
print('Print table using user input')
l=int(input('Enter the number for the table : '))
for i in range(1,11):
    print(l,' * ',i,' = ',l*i)
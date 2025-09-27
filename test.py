## Lambda function
#print((lambda y: y-9)(8))
#print((lambda : 6-9)())
'''
n=[('Mohan',37),('Rajee',35),('Krish',10),('Akshara',2)]
while True:
    x = input("Enter numeric value to get the out output of result , press n/N to exit from program :   ")
    if x.lower()=='n':
        print("Exiting program...")
        break
    else:
        try:
            print(n[int(x)])
        except ValueError:
            print("❌ Invalid number. Please enter numeric values only.")
        except Exception as e:
            print(f"Out of index given {e}")
'''
import csv
import os

print(os.getcwd())
os.chdir(r'D:\python\code')
print(os.getcwd())
file_name = r'D:\python\code\test.csv'  # Use raw string for Windows path
with open(file_name, mode='r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    headers = next(csvreader)  # Read header row
    print("Headers:", headers)

    for row in csvreader:
        print(row)
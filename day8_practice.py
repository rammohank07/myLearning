'''def sum_digits():
    while True:
        try:
            num=input("Enther the number to get the sum of digitis, enter 0 to exit from program:   ").strip()
            sum_digit = 0
            if num=='0':
                print("Exiting the program...")
                break
            if int(num)<0:
                print("enter only positive numbers")
            else:
                for i in num:
                    sum_digit=sum_digit+int(i)
                print(f"Sum of digits of given number {num} is {sum_digit}")
        except Exception as e:
            print(f"Invalid number entered, {e}")
sum_digits()
def get_factorial():
    while True:
        try:
            num=input("Please enter the number, enter exit to exit from progrsme  : ").strip()
            if num=='0':
                print(f'Factorial of given number {num}! is 1')
                continue
            if num.lower()=='exit':
                print("Exiting from program!...")
                break
            if int(num)<0:
                print(f" Please enter only positive numbers to get factorial of number, the given input {num} is not a positive number")
            else:
                num=int(num)
                fact = 1
                for i in range(num):
                    fact=fact*(num-i)
                print(f"Factorial of given number {num}! is {fact}")
        except Exception as e:
            print(f"Error while executing program {e}")
get_factorial()
def check_polindrem():
    while True:
        try:
            str_p=input("Enter the word to check polindrem, enter exit to exit from program!:  ").strip().lower()
            if str_p.lower()=='exit':
                print("Exitig from program...")
                break
            else:
                str_r=str_p[::-1]
                #for i in str_p:
                    #str_r=i+str_r
                if str_r==str_p:
                    print(f" The Given word {str_p} is polindram ")
                else:
                    print(f" The Given word {str_p} is not polindram ")
        except Exception as e:
            print("Error while executing program {e}   ")
check_polindrem()
def get_even_odd():
    n=3
    while n>0:
        try:
            num=input("Please enter the number to check even or odd:   ").strip()
            num=int(num)
            if num%2==0:
                print(f"The gien number {num} is a EVEN number")
            else:
                print(f"The gien number {num} is a ODD number")
            n=n-1
        except ValueError:
            print(f"PLease enter only numeric values, you have entered {num}")
        except Exception as e:
            print(f"Error while executing program {e}")
get_even_odd()
def get_fact():
    while True:
        try:
            num=input(" Please enter the positive number to get factorial, press exit to exit from program: ").strip().lower()
            if num=='exit':
                print("Thanks for using the factorial program!, Exiting from the program...")
                break
            num = int(num)
            if num<0:
                print(f"Number should not be negative, you have entered {num}.")
                print()
                continue
            else:
                fact=1
                for i in range(1,num+1):
                    fact=(fact*i)
                print(f"Factorial of given number {num} is {fact}")
                print()
        except ValueError:
            print(f"Invalid number {num} entered, please enter only positive numbers")
            print()
        except Exception as e:
            print(f"Error while executing the program!, ")
            print()
            continue
get_fact()

def get_Fibonacci():
    while True:
        try:
            num=input("Enter the number to get fibonacci.  ").strip().lower()
            print()
            if num=='exit':
                print("Thank you so much for using this program to get fibonacci series!.")
                print()
                break
            num=int(num)
            if num<0:
                print(f"Please enter only positive numbers to get febonacci series, you have entered {num}")
                print()
                continue
            else:
                fibo_p=0
                fibo_c=1
                fibo_s='0'
                for i in range(num-1):
                    fibo_n=fibo_p+fibo_c
                    fibo_p=fibo_c
                    fibo_c=fibo_n
                    fibo_s=fibo_s+' '+str(fibo_n)
                print(f"Fibonacci series of given number {num} is {fibo_s}")
                print()
        except ValueError:
            print(f"Invalid number {num} entered, please enter only positive number")
            print()
            continue
        except Exception as e:
            print(f"Error while executing the program! {e}")
            print()
            continue
get_Fibonacci()
'''
def get_marks():
    s_dist={}
    high_score = 0
    top_name = ''
    try:
        num=input("Enter the number of students data need to add?   ").strip()
        print()
        if not num.isdigit():
            print(f"Please enter positive number only for studetns, you have entered as {num}")
            return
        num=int(num)
        if num <= 0:
            print(f"Please enter the number more than 0. you have entered {num}")
            return
    except ValueError:
        print(f"Please enter only positive number, you have entered as {num}")
        print()
    except Exception as e:
        print(f"Please enter only positive number, you have entered as {e}")
        print()
    for i in range(num):
        try:
            s_name=input("Enter {i+1} student name: ").upper()
            print()
            if s_name.isdigit():
                print(f"Please enter name in alpha numeric or alabit only, you have entered as numeric {s_name} ")
                continue
        except Exception as e:
            print(f"Error occured  in student name {e}")
            continue
        s_marks=input("enter three subjects marks with space in between .  ").strip().split()
        if len(s_marks)!=3:
            print(f"Please enter three subjects marks, you entered {s_marks}")
            print()
            continue
        try:
            s_marks=list(map(int,s_marks))
            s_dist[s_name] =s_marks
        except Exception as e:
            print(f"Error occured in the marks conversion {e}")
            print()
    print(f"Student details are {s_dist}")
    for key, value in s_dist.items():
        total = sum(value)
        avg_val = total / len(value)
        print(f"{key} → Total: {total}, Average: {avg_val:.2f}")
    if total > high_score:
        high_score = total
        top_name = key
    print(f"\nTop Scorer: {top_name} with marks {high_score}")
    # Subject-wise highest marks
    if s_dist:
        maths_top = max(s_dist.items(), key=lambda x: x[1][0])
        science_top = max(s_dist.items(), key=lambda x: x[1][1])
        english_top = max(s_dist.items(), key=lambda x: x[1][2])

        print(f"\n🏆 Overall Top Scorer: {top_name} with total marks {high_score}\n")
        print("=== Subject-wise Toppers ===")
        print(f"Maths → {maths_top[0]} ({maths_top[1][0]} marks)")
        print(f"Science → {science_top[0]} ({science_top[1][1]} marks)")
        print(f"English → {english_top[0]} ({english_top[1][2]} marks)")
        print()


get_marks()
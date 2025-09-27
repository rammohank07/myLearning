def get_positive():
    while True:
        try:
            n=int(input(" Enter positive number only! :  "))
            if n<0:
                print(f"The given humber {n} is not a positive number, PLease enter positive number only")
            else:
                return f" The given number  {n} is positive number"
        except ValueError:
            print("Invalid Number Entered!")
print(get_positive())
print('check the min,max , avg of given numbers')
def get_number():
    try:
        n=input(" Enter the multiple number with space between ").strip().split()
        n=[float(i) for i in n]
        print(n)
        return max(n),min(n), (sum(n)/len(n))
    except ValueError:
        print("Invalid number")

max_val,min_val,avg_val=get_number()
print("Max Value ",max_val, "nmin_val ", min_val, " Avg value ", avg_val)
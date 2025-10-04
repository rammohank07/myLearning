def get_mynum():
    l = []
    while True:
        try:
            n=input("Enter Numbers and exit if want to exit from program:   ")
            if n=='exit':
                print('Exiting from the program...')
                break
            else:
                l.append(l)
                #l= l+' '+n
        except ValueError:
            print("Invalid number")
        except Exception as e:
            print(f"Error Occured   {e}")
    l=l.strip().split()
    num=[float(i) for i in l]
    return min(num),max(num),(sum(num)/len(num))
min_val,max_val,avg_val=get_mynum()
print(f"Minimum value if {min_val},Maximum value is {max_val}, Average value is {avg_val}")

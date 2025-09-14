## Mimi project with python basics
'''
import datetime
def Personal_Dairy():
    print("\n Personal Dairy App")
    while True:
        ## Providing optionsto users
        print("\n 1. Add New Entry")
        print("\n 2. View All Entries")
        print("\n 3. Search Entries by Date")
        print("\n 4. Exit")
        choice =int(input("\n PLease enter your number to select your choice(1:4)  :  "))
        if choice==1:
            file=open("Dairy.txt","a")
            usr_inpt=input(" Ente the text into the dairy")
            dt=datetime.datetime.now().strftime('%Y-%M-%D %H:%M:%S')
            file.write(f"[{dt}] {usr_inpt}\n")
        elif choice==2:
            file=open("Dairy.txt","r")
            lines = file.readlines()
            print(lines)
        elif choice==3:
            search_word =input("Enter word to search : ")
            file=open("Dairy.txt", "r")
            lines = file.readlines()
            for line_number, line in enumerate(lines, start=1):
                if search_word in line:
                    print(f"Found '{search_word}' in line {line_number}: {line.strip()}")
        elif choice==4:
            print("\n Succesfully exit from dairy!")
            break
Personal_Dairy()
'''
import datetime

def Personal_Diary():
    print("\n📓 Personal Diary App")
    while True:
        print("\n1. Add New Entry")
        print("2. View All Entries")
        print("3. Search Entries by Date")
        print("4. Exit")

        choice = int(input("\nPlease enter your number (1-4): "))

        if choice == 1:
            usr_inpt = input("Enter the text into the diary: ")
            dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open("Diary.txt", "a") as file:
                file.write(f"[{dt}] {usr_inpt}\n")
            print("✅ Entry saved!")

        elif choice == 2:
            try:
                with open("Diary.txt", "r") as file:
                    lines = file.readlines()
                    if not lines:
                        print("No entries yet!")
                    else:
                        print("\n--- All Diary Entries ---")
                        for line in lines:
                            print(line.strip())
            except FileNotFoundError:
                print("❌ No diary file found. Add an entry first!")

        elif choice == 3:
            search_date = input("Enter date to search (YYYY-MM-DD): ")
            try:
                with open("Diary.txt", "r") as file:
                    lines = file.readlines()
                    found = False
                    for line_number, line in enumerate(lines, start=1):
                        if search_date in line:
                            print(f"Found entry in line {line_number}: {line.strip()}")
                            found = True
                    if not found:
                        print(f"No entries found for date {search_date}")
            except FileNotFoundError:
                print("❌ No diary file found. Add an entry first!")

        elif choice == 4:
            print("\n✅ Successfully exited from diary!")
            break

        else:
            print("❌ Invalid choice! Please select 1-4.")

# Run the diary app
Personal_Diary()



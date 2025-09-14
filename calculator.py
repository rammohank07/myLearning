import math


def calculator():
    while True:
        print("\n--- Python Math Calculator ---")
        print("1. Square Root")
        print("2. Factorial")
        print("3. Power (x^y)")
        print("4. Logarithm (log base b of x)")
        print("5. Floor")
        print("6. Ceil")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            n = float(input("Enter a number: "))
            print(f"Square root of {n} is {math.sqrt(n)}")

        elif choice == "2":
            n = float(input("Enter an integer: "))
            if n.is_integer() and n >= 0:
                print(f"Factorial of {int(n)} is {math.factorial(int(n))}")
            else:
                print("❌ Factorial is only defined for non-negative integers!")

        elif choice == "3":
            x = float(input("Enter base (x): "))
            y = float(input("Enter exponent (y): "))
            print(f"{x} to the power of {y} is {math.pow(x, y)}")

        elif choice == "4":
            x = float(input("Enter the number: "))
            b = float(input("Enter the base: "))
            if x > 0 and b > 0 and b != 1:
                print(f"log base {b} of {x} is {math.log(x, b)}")
            else:
                print("❌ Logarithm requires x > 0, base > 0 and base != 1")

        elif choice == "5":
            n = float(input("Enter a number: "))
            print(f"Floor of {n} is {math.floor(n)}")

        elif choice == "6":
            n = float(input("Enter a number: "))
            print(f"Ceil of {n} is {math.ceil(n)}")

        elif choice == "7":
            print("✅ Exiting calculator. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please select between 1-7.")


# Run the calculator
calculator()

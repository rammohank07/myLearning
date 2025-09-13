## Creating a function in python
'''
def greet_user():
    print('Hello',' Welcome to python coding')
greet_user()
'''

## Creating mathematical function to perform badic mathematical operations
def math_fun():
    def add_fun(a, b):
        try:
            return f"Addition of two numbers is: {a + b}"
        except Exception as e:
            return f"❌ Error while adding: {e}"

    def sub_fun(a, b):
        try:
            return f"Subtraction of two numbers is: {a - b}"
        except Exception as e:
            return f"❌ Error while subtracting: {e}"

    def mul_fun(a, b):
        try:
            return f"Multiplication of two numbers is: {a * b}"
        except Exception as e:
            return f"❌ Error while multiplying: {e}"

    def div_fun(a, b):
        try:
            return f"Division of two numbers is: {a / b}"
        except ZeroDivisionError:
            return "❌ Error: Division by zero is not allowed."
        except Exception as e:
            return f"❌ Error while dividing: {e}"

    # Step 1: Get valid operation
    while True:
        choice = input("Enter operation (add/sub/mul/div/all): ").strip().lower()
        if choice in ["add", "sub", "mul", "div", "all"]:
            break
        else:
            print("❌ Invalid choice. Please enter 'add', 'sub', 'mul', 'div', or 'all'.")

    # Step 2: Get valid numbers
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            break
        except ValueError:
            print("❌ Invalid number. Please enter numeric values only.")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

    # Step 3: Perform operation
    try:
        if choice == "add":
            return add_fun(a, b)
        elif choice == "sub":
            return sub_fun(a, b)
        elif choice == "mul":
            return mul_fun(a, b)
        elif choice == "div":
            return div_fun(a, b)
        else:  # all
            results = [
                add_fun(a, b),
                sub_fun(a, b),
                mul_fun(a, b),
                div_fun(a, b)
            ]
            return "\n".join(results)  # formatted nicely
    except Exception as e:
        return f"❌ Calculation failed: {e}"





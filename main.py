# main.py
from add import add
from subtract import subtract
from multiply import multiply
from division import divide

def calculator():
    print("Simple Calculator")
    print("Options: add, sub, mul, div, exit")
    
    while True:
        choice = input("Choose operation: ").lower()
        if choice == "exit":
            print("Bye!")
            break
        if choice not in ["add", "sub", "mul", "div"]:
            print("Invalid choice!")
            continue

        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == "add":
            print(f"Result: {add(x, y)}")
        elif choice == "sub":
            print(f"Result: {subtract(x, y)}")
        elif choice == "mul":
            print(f"Result: {multiply(x, y)}")
        elif choice == "div":
            print(f"Result: {divide(x, y)}")

if __name__ == "__main__":
    calculator()
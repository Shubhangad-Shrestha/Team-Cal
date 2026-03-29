def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero!")
        return None
    return a / b

def divide_menu():
    print("\n===== DIVISION =====")
    print("1. Division   (a / b)")
    print("2. Floor Div  (a // b)")
    print("3. Modulo     (a % b)")
    print("0. Back")
    print("====================")

    choice = input("Select: ").strip()
    if choice == "0":
        return

    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
    except ValueError:
        print("Invalid input! Numbers only.")
        return divide_menu()

    if b == 0:
        print("Error: Cannot divide by zero!")
        return

    if choice == "1":
        print(f"{a} / {b} = {a / b}")
    elif choice == "2":
        print(f"{a} // {b} = {a // b}")
    elif choice == "3":
        print(f"{a} % {b} = {a % b}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    while True:
        divide_menu()
        if input("\nAgain? (y/n): ").lower() != "y":
            break
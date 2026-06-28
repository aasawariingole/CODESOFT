while True:
    print("\n===== Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Calculator Closed")
        break

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Answer =", num1 + num2)

        elif choice == "2":
            print("Answer =", num1 - num2)

        elif choice == "3":
            print("Answer =", num1 * num2)

        elif choice == "4":
            if num2 != 0:
                print("Answer =", num1 / num2)
            else:
                print("Division by zero is not possible.")

    else:
        print("Invalid Choice")

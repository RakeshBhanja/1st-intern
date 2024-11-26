print("  / * - + SIMPLE CALCULATOR + _ * /")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

choice = input("Enter your operator +, -, *, / : ")

if choice == "+":
    print("Result:",num1 + num2)
elif choice =="-":
    print("Result:",num1 - num2)
elif choice =="*":
    print("Result:",num1 * num2)
elif choice =="/":
    if num2 != 0:
     print("Result:",num1 / num2)
    else:
      print("error division by zero")
else:
    print|("Invalid input")
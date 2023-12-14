a=int(input("Enter first value:"))
b=int(input("Enter second value:"))

print("\nChoose the operation: 1/2/3/4/5 \n"
      "1=Addition\n"
      "2:Subtraction\n"
      "3:Multiplication\n"
      "4:Division\n"
      "5:Exit\n")
choice=1
while choice!=5:

    choice = int(input("Enter your choice:"))
    match choice:

        case 1:
            result = a + b
            print("Addition:", result)

        case 2:
            result = a - b
            print("Subtraction:", result)
        case 3:
            result = a * b
            print("Multiplication:", result)
        case 4:
            result = a / b
            print("Division:", result)
        case 5:
            print("\nThank you!\U0001F607")
        case _:
            print("\nEnter No. between 1-5\n")
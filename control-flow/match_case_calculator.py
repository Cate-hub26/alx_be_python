num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose your operation (+, _, *, /): ")

match operation:
    case addition:
        if operation == "+":
            result = num1 + num2
            print(f"The result is {result}.")
      
match operation:           
    case subtract:
        if operation == "-":
            result = num1 - num2
            print(f"The result is {result}.")
            
match operation:           
    case multiply:
        if operation == "*":
            result = num1 * num2
            print(f"The result is {result}.")

            
match operation:           
    case divide:
        if operation == "/" and num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Cannot divide by zero.")


            

            
    
        


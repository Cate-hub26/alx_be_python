num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose your operation (+, _, *, /): ")

match num1 | num2:
    case operation1:
        if operation == "+":
            result = num1 + num2
            print(f"The result is {result}.")
      
match num1 | num2:           
    case operation2:
        if operation == "-":
            result = num1 - num2
            print(f"The result is {result}.")
            
match num1 | num2:           
    case operation3:
        if operation == "*":
            result = num1 * num2
            print(f"The result is {result}.")
            
match num1 | num2:           
    case operation4:
        if operation == "/" and num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Cannot divide by zero")


            

            
    
        


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

chosen_operation = input("Choose your operation (+, -, *, /): ")

match chosen_operation:
    case "+":
            result = num1 + num2
            print(f"The result is {result}.") 
    case "-":
            result = num1 - num2
            print(f"The result is {result}.")               
    case "*":
            result = num1 * num2
            print(f"The result is {result}.")  
    case "/":
        if chosen_operation == "/" and num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Cannot divide by zero.")


            

            
    
        


            


            

            
    
        


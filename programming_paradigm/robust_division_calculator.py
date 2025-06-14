def safe_divide(numerator, denominator):

    try:
        return numerator / denominator
    
    except ZeroDivisionError as e:
        return "Cannot divide by zero."
        
    except ValueError as e:
        return e
    


        
        
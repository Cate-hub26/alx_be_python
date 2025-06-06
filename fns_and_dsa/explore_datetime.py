import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    print(current_date)

    def calculate_future_date():
        future_date = current_date + timedelta(days=10)
        print(future_date)
    
    calculate_future_date()      
    
display_current_datetime()

    

    
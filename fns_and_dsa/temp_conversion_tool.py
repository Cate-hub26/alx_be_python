FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius():
        return (temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        
def convert_to_fahrenheit():
        return (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        
temperature = float(input("Enter the temperature to convert: "))
units = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if units == "F":
    temperature_to_celsius = convert_to_celsius()
    print(f"{temperature}°F is {temperature_to_celsius}°C")
    
elif units == "C":
    temp_to_fahrenheit = convert_to_fahrenheit()
    print(f"{temperature}°C is {temp_to_fahrenheit}°F")
    
else:
    print("Invalid temperature. Please enter a numeric value.")
      
    

        

        
        
class Calculator:
    calculation_type = "Arihmetic Operations"
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation_type: {cls.calculation_type}")
        return a * b
    
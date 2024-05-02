from typing import Callable

def multiply_setup(a: float) -> Callable:
    
    def multiply(b: float) -> float:
        
        return a * b
    
    return multiply

double = multiply_setup(2)

print(double(100))
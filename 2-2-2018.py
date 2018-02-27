"""
Recursion - every call of the function, the PVM must allocate a stack to the stack frame, this stack contains
the value of the arguments, the return address for a particular call, and space for the return value.

Namespace - a program's set of its variables and their values - can be controlled

Optional parameters - located at the end of parameter list, optional if assigned a default value.

*****Higher order functions:*****
"""
import math

def demo_function_temp_var(x: int) -> None:
    f = abs
    print("Absolute value f(x) = ", f(x))

def demo_function_parameter(f, x: int) -> int:
    return f(x)

def main() -> int:
    demo_function_temp_var(-4)
    y = demo_function_parameter(abs, -4)
    print("Absolute value f(x) = ", y)
    y = demo_function_parameter(math.sqrt, 4)
    print("Square root of f(x)", y)
    return 0

if __name__ == '__main__':
    main()

"""
Mapping - applies a function to each value and returns a new sequence of the results

Filtering - a function that returns T/F, called a predicate, is applied to each value in the list, returns true values
"""

#Reducing - take a list of values, repeatedly applies a function, accumulates a single data value.
data = [1,2,3,4]
reduce(add,data)
reduce(multiply,data)


#Lambda - specify addition or multiplication on the fly

data = [1,2,3,4]
reduce(lambda x, y: x+y), data)



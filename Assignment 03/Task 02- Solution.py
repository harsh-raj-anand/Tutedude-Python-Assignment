import math

num = float(input("Enter a number: "))

if num <= 0:
    print("Please enter a positive number for square root and logarithm.")
else:
    squareRoot = math.sqrt(num)
    log = math.log(num)
    sin = math.sin(num)

    print("Square root:", squareRoot)
    print("Logarithm:", log)
    print("Sine:", sin)

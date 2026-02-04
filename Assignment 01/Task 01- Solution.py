num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2

if num2 != 0:
    div = float(num1) / float(num2)
else:
    div = "Undefined (division by zero)"

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)

print("Division:", round(div,2))

print("Hello guys this is my Calcultor program\n")
a = float(input("Enter your first number here: "))
b = float(input("Enter your second number here: "))
input_1 = input("""
What arthematic opration do you want to perform?\n
press "*" to multiply,\n
press "/" to divide,\n
press "+" to add,\n
press "-" to subtract
: """)
# print("0")
if input_1 == "*":
    print(a*b)
elif input_1 == "/":
    print(a/b)
elif input_1 == "+":
    print(a+b)
elif input_1 == "-":
    print(a-b)
else:
    print("Retry")
# Insecure code: using eval() unsafely
def calculate_expression(expression):
    return eval(expression)

user_input2 = input("Enter a mathematical expression: ")
print(calculate_expression(user_input2))

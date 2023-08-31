def bigger_of_three(num1,num2,num3):
    if num1>num2:
        y=num1
    else:
         y=num2
    
    if num3>y:
        print(f"{num3} is greatest of all")
    else:
        print(f"{y} is greatest of all")

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

bigger_of_three(num1,num2,num3)

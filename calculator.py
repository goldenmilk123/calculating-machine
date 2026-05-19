num1 = float(input("enter the number:" ))
operator = input("enter the operator(+,-,%,X): ")
num2 = float(input("enter the number:" ))
if operator == "+":
  print(num1 + num2)
elif operator == "-":
  print(num1 - num2)
elif operator == "%":
  print(num1 / num2)
elif operator == "X":
  print(num1 * num2)

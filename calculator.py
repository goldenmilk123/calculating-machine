import re
def calculate(expression):
    tokens = re.findall(r'\d+|\+|\-|\*|\/', expression.replace(" ",""))
    output = []
    operators = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    for tokens in tokens:
        if tokens.isdigit():
            output.append(int(tokens))
        else:
            while operators and precedence.get(operators[-1], 0) >= precedence[tokens]:
                output.append(operators.pop())
              operators.append(tokens)
            operators.append(tokens)
          while operators:
            output.append(operators.pop())
            stack = []
            for token in output:
                if isinstance(token, int):
                    stack.append(token)
                else:
                    if len(stack) < 2:
                        return "Error"
                    num2 = stack.pop()
                    num1 = stack.pop()
                    if token == '+':
                        stack.append(num1 + num2)
                    elif token == '-':
                        stack.append(num1 - num2)
                    elif token == '*':
                        stack.append(num1 * num2)
                    elif token == '/':
                        if num2 == 0:
                            return "Error: Division by zero"
                        stack.append(num1 / num2)
    return stack[0] if stack else 0
user_input = input("Enter a mathematical expression: ")
result = calculate(user_input)
print("Result:", result)
                
    
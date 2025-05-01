def eva_postfix(expression):
    stack = []
    operators = {'+': lambda a, b: a+b,
                 '-': lambda a, b: a-b,
                 '*': lambda a, b: a*b,
                 '/': lambda a, b: a/b,}

    tokens = expression.split()
    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            result = operators[token](a, b)
            stack.append(result)
        else:
            stack.append(float(token))

    return stack.pop()


print(eva_postfix("5 3 + 2"))


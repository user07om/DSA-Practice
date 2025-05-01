def inf_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '~': 3}
    stack = []
    result = []

    for char in expression:
        if char.isalnum():
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')': 
            while stack and stack[-1] != '(':
                result.append(stack.pop())
                
            if stack and stack[-1] == '(':
                stack.pop()

        else:
            while stack and stack[-1] != '(' and (char not in precedence or precedence.get(char, 0) <= precedence.get(stack[-1], 0)):
                result.append(stack.pop())
            stack.append(char)


    while stack:
        result.append(stack.pop())
    
    return ''.join(result)

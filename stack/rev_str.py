def rev_str(input_str):
    stack = []
    for char in input_str:
        stack.append(char)
    
    rev_str = ""
    while stack:
        rev_str += stack.pop()

    return rev_str

print(rev_str("omkar"))




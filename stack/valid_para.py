def is_balanced(given_input):
    stack = []
    set_brackets = {')': '(', '}': '{', ']': '['}

    for char in given_input:
        if char in "({[":
            stack.append(char)
        elif char in "]})":
            if not stack:
                return False
            top_para = stack.pop()
            if top_para != set_brackets[char]:
                return False
    print(stack)
    return len(stack) == 0
            


given_input = "()[]"
print(is_balanced(given_input))

def eva_postfix(expression):
    stack = []
    operators = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b, 
            '*': lambda a, b: a*b, 
            '/': lambda a, b: a/b, 
            }
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


print(eva_postfix("5 2 + 2 *"))


#sorting algo practice (bubble sort, quick sort, selection sort)
def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


def selection_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        min_idx = i
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[min_idx]:
                min_idx = j
                swapped = True

            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    if not swapped:
        return arr

print(selection_sort([2, 1, 4, 3]))

"""
before moving, lets descuss what is stack.. in simple way. it's an data-structure which stores the data in LIFO format (Last In First Out), as an example stack of books or dishes. you cannot grap the bottom one until you finish the top one first. there are four methods use here, 
1. append(add data at end). 
2. pop(remove top-most data). 
3. isEmpty(checks is stack empry or not)
4. peak(get the last element, top of stack)
"""

class Stack:
    def __init__(self):
        self.arr = {}
        self.top = -1

    def append(self, val: int) -> None:
        self.top += 1
        self.arr[self.top] = val

    def pop(self) -> int:
        if self.top == -1:
            return None
        ele = self.arr[self.top]
        del self.arr[self.top]
        self.top -= 1

        return ele

    def peak(self) -> int:
        if self.top == -1:
            return None
        return self.arr[self.top]

    def is_empty(self) -> bool:
        return self.top == -1

    def display(self) -> list[int]:
        return [self.arr[i] for i in range(self.top + 1)]



stack = Stack()
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()
print(stack.peak())
print(stack.is_empty())
print(stack.display())


#FIRST QUESTION - VALID PARA
def valid_para(s: str) -> bool:
    para_sets = {')': '(', '}': '{', ']': '['} 
    visited: list[str] = []
    for c in s:
        if c in "([{":
            visited.append(c)
        elif c in ")]}" and para_sets[c] == visited[-1]:
            visited.pop()
    return len(visited) == 0

print(valid_para("()[]{}"))

def reverse_str(s: str) -> str:
    rev_str = []
    s = list(s)
    for _ in range(len(s)):
        rev_str.append(s.pop())

    return "".join(rev_str)

print(reverse_str("omkar"))


class minStack:
    def __init__(self):
        self.arr = {}
        self.top = -1
        self.min_stack = {}
        self.min_ele = float("inf")

    def push(self, val):
        self.top += 1
        self.arr.append(val)

        if 

        #insert the element in the array

    def pop(self):
        if self.top == -1:
            return None
        ele = self.arr[self.top]
        del self.arr[self.top]
        del self.arr[-1]
        self.top -= 1

        return ele


    def get_min(self):
        return self.min_ele

    def display(self):
        return [self.arr[i] for i in range(self.top+1)]



mick = minStack()
mick.push(5)
mick.push(3)
mick.push(2)
mick.push(1)
mick.pop()
mick.pop()

print("minStack: ", mick.display())
print("minStack: ", mick.get_min())
#print(mick.get_min())


#problem 3 - valid paranthesis II
def vali_para_two(s: str) -> bool:
    para_set = {')': '(', ']': '[', '}': '{'}
    visit = []
    i = 0
    while i < len(s): 
        if s[i].isalnum(): 
            i += 1
            continue


        if s[i] in "({[":
            visit.append(s[i])
            i += 1
        elif len(visit) == 0: return False
        elif s[i] in ")]}" and para_set[s[i]] == visit[-1]:
            visit.pop()
            i += 1


    return len(visit) == 0

print(vali_para_two("()abc"))


#problem 4 - k[string]: decode string.

def decode_str(s: str) -> str:
    # the actual logic is k[string] means repeat string k times.
    res = []
    i = 0
    
    k = float("inf")
    while i < len(s):
        if s[i] in "123456780":
            k = s[i]


        if s[i] == "[" and i > 0:
            c = s[i+1]

            #for creating the str of chars: for adding to the res.
            i += 2
            while s[i] not in "[]" and s[i] not in "123456780":
                c += s[i]
                i += 1

            #res.append(c)
            #add to the res list
            for _ in range(int(k)):
                res.append(c)

            if s[i] in "123456780":
                k = s[i]
                i += 1
                continue


        i += 1

    return "".join(res)
        
print(decode_str("2[a3[b]]"))



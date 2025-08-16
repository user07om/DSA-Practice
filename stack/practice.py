class Stack:   #BESIC STACK IMPLEMENTATION.
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def size(self):
        return len(self.stack)



# linked list stack based implementation.
class Node:
    def __init__(self):
        self.value = value
        self.next = None


class StackLL:
    def __init__(self):
        self.top = None 
        self.length = 0


    def push(self, value):
        node = Node(value) #assing the Node object to the node variable - node.value, node.next
        node.next = self.top  #assign the None to the node.next 
        self.top = node # assing self.top as node object.
        self.length += 1  # increase the lenght


    def pop(self):
        if self.top is None:  # if no vairable assing, which top has the object Node(val, next) as default val 
            return None
        val = self.top.value  # store the top.val to val.
        self.top = self.top.next # assing the None, means the 
        self.length -= 1 #decrease the length by one
        return val # return the val.


    def peek(self):
        return self.top.value if self.top else None

    def is_empty(self):
        return self.top is None 

    def size(self):
        return self.length


print("Hello World! ----------------")

# -- hash-set practice (create, add, remove and search)
fruits = set()

#add the item in the set (it will add randomely not it stack way!) 
fruits.add("apple")
fruits.add("banana")
fruits.add("cherry")

#remove the item from the set.
#fruits.remove("apple")
#fruits.discard("apple")

#search in set.
print(f"is apple is is set: {"appe" in fruits}")

print(fruits)
for fruit in fruits:
    print(fruit)



# set operations ----
num1 = {1, 2, 3, 4}
num2 = {3, 4, 5, 6}

print(f"union {num1 | num2}")  # removes dublicates.
print(f"intersection {num1 & num2}") # both has the same numbers
print(f"differences {num1 - num2}")  # first set numbers that not invlolve in second one
print(f"symatric differences {num1 ^ num2}")  #both set numbers which are unique.



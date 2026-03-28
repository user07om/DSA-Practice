class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        return None

    def isEmpty(self):
        return len(self.data) == 0

    def front(self):
        return None if self.isEmpty() else self.data[0]

    def size(self):
        return len(self.data)

    def show_data(self): return self.data


q = Queue()
q.enqueue(4)
q.enqueue(2)
q.enqueue(1)

print(q.show_data())
q.dequeue()
print(q.show_data())
print(q.size())


        
#pythonic way using collections!
from collections import deque

q = deque()
q.append(10) #enque
q.append(20)
q.append(30)

print(q)
q.popleft() #deque.
print(q)  
print(q[0]) #front.


#semulation: using queue from the collection module!
line = deque(["A", "B", "C", "D"])

line.popleft()   #served the "A"
line.append("E") #"E" joins
line.popleft()   #served the "B"
line.append("F") #"F" joins

print(line)

#Queues - Order preservation machine!

#classic patterns - reverse a queue

def reverse_queue(q):
    stack = []
    while q:
        stack.append(q.popleft())

    while stack:
        q.append(stack.pop())

    return q 

q = deque([1, 2, 3, 4])
print(reverse_queue(q))




    



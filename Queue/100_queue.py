"""
so queue is like of people in line, where the first one in line will be served first and the new person will enter at end of line (rear). there are meanly 4 operations in queue.
1. front (remmove the first one fromt he queue) it also know as dequeu()
2. rear (add the element at the end of the line) it also know as enqueu()
3. is-empty (return the bool value as)
4. peak (returns the first one in the queue)

"""

class Queue:
    def __init__(self):
        self.arr = {}
        self.front = 0
        self.rear = -1

    def enque(self, val):
        self.rear += 1
        self.arr[self.rear] = val

    def deque(self):
        if self.rear == -1:
            return None
        ele = self.arr[self.front]
        del self.arr[self.front]
        self.front += 1

        return ele

    def peak(self):
        if self.rear == -1:
            return None
        return self.arr[self.front]

    def is_empty(self):
        return self.rear == -1

    def display(self):
        return [v for v in self.arr.values()]
    

que = Queue()
que.enque(1)
que.enque(2)
que.enque(3)
que.enque(4)
que.deque()
que.deque()

print(que.display())


#PROBLEM:  FIRST NON-REPEATING CHARACTER

def problem(s: str) -> str:
    freq = {}
    queue: list[str] = []
    i = 0
    j = -1

    for c in s:
        #DEQUE 
        v = c
        del c
        i += 1

        #ENQUE
        queue.append(v)
        j += 1

        if v not in freq:
            freq[v] = 1
        else: freq[v] += 1

        if s[i] == queue[j]:
            continue
        else:
            return v

    return -1

print(problem("aabbc"))

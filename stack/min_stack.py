class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, item):
        self.stack.append(item)

        if not self.min_stack or self.stack[-1] <= self.min_stack[-1]:
            self.min_stack.append(item)


    def pop(self):
        if not self.stack:
            return None

        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()

        return self.stack.pop()

    def display(self):
        print(f"normal stack -> {self.stack}\nmin stack -> {self.min_stack}")


min_stack = MinStack()
min_stack.push(2)
min_stack.push(4)
min_stack.push(1)

min_stack.display()

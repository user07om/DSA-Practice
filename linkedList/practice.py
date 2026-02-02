class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# practice whitout any linked list ---
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node1

print(node1.data, node1.next.data, node2.next.data )
print(f"---------{node1.data}, {node2.data}, {node3.data}")
print(f"---------{node1.data}, {node1.next.data}, {node1.next.next.data}")


#while node1:
    #print(node1.data, end=" ")

#last_node = node1
#while last_node.next:
#    if last_node is None:
#        break
#    print("yoo ", last_node.data)
#    last_node = node1.next


def print_node(node):
    if node is None:
        return
    print(node.data, end="-")
    print_node(node.next)

#print_node(node1)

print("------")

#floye'ds cycle detection (fast and slow)
# cycle detection.
def cycle_det(node):
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

print(cycle_det(node1))

print("------")


# the linked list class class with first approach where insertion is O(n).
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next


# the linked list with secon approach where insertion is O(1)
class linkedList_two:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pre_append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

    def insert_pos(self, idx, data):
        if idx == 0:
            self.pre_append(data)
            return

        new_node = Node(data)
        curr_node = self.head
        for _ in range(idx-1):
            if curr_node is None:
                print("position out of bounds")
                return
            
            curr_node = curr_node.next
        
        new_node.next = curr_node.next
        curr_node.next = new_node
                



    def display(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next 


#linked = LinkedList()
#linked.append(9)
#linked.append(4)
#linked.append(8)
#linked.display()


linked_two = linkedList_two()
linked_two.append(3)
linked_two.append(2)
linked_two.append(7)
linked_two.pre_append(1)
linked_two.insert_pos(2, 9)
linked_two.display()



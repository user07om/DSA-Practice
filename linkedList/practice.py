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

print(node1.data, node1.next.data, node2.next.data )


# the linked list class for methods.
class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # FIRST APPROCH WOULD BE LKE THIS!
    def append(self, data):
        new_node = Node(data)   # initialize the new_node to Node class with data init.
        if self.head is None:   # checks - if self.head is None then it will assign the new_node to it.
            self.head = new_node
            return

        last_node = self.head   # if self.head is not None, it assing the self.head to last_node and iterate over it till None.
        while last_node.next:   # breaks when last_node means self.head nexts becomes None
            last_node = last_node.next  # till now it will assign the next points mean next node to last node to keep the race 
        last_node.next = new_node  # once the break ends then last_node.next points to new_node 
    # --------------------


    # SECOND APPROCH WOULD BE!
    def appendS(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head # its' same as above - we just have to reach the None means node.next, possible via while loop
        while current:
            print(current.data, end=" -> ")  # preint the current node data.
            current = current.next  # and point the curren tnode to it's next node for continueing the loop.
        print(None)


linked = linkedList()
linked.appendS(3)
linked.appendS(4)
linked.appendS(8)
linked.display()


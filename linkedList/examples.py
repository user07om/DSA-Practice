class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_end(self, data):   #FIRST APPROACH
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def append_end_two(self, data): #SECOND APPROACH
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_first(self, data):
        """
        insert at first: 
            1. we assign the new_node to head pointer
            2. new_node next pointer to head 
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node


    def insert_at_pos(self, idx, data):
        """
        1. initialize the new node.
        2. iterate over the nodes till position.
        3. ...
        """
        new_node = Node(data)
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head
        for _ in range(idx-1): #if you want to follow numbering indexes then 2 else programing ways 1.
            temp = temp.next
        
        new_node.next = temp.next
        temp.next = new_node





    def display_nodes(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next


#insert at position



link_is = LinkedList()
link_is.append_end_two(1)
link_is.append_end_two(3)
link_is.append_end_two(2)
link_is.insert_first(0)
link_is.insert_at_pos(0, 4)
link_is.display_nodes()

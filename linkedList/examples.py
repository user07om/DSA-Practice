class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def push_back(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop_front(self):
        if self.head is None:
            print("linked list is empty! cannot pop_front")
            return

        temp = self.head
        self.head = temp.next

        if self.head is None:
            self.tail = None

        return temp

    def pop_back(self):
        if self.head is None:
            print("linked list is empty! cannot pop_back!")
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        temp = self.head
        while temp.next != self.tail:
            temp = temp.next

        val = self.tail.data
        self.tail = temp
        self.tail.next = None

        return val

    def insert(self, pos, val):
        if pos < 0:
            print("enter valid position please!")
            return
        
        if pos == 0:
            self.push_front(val)
            return

        new_node = Node(val)
        temp = self.head
        idx = 1
        while idx != pos:
            if temp is None:
                print("invalid pos!")
                return
            temp = temp.next
            idx += 1
        
        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        if self.head is None: print("linked list is empty!")
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


if __name__=="__main__":
    ll = LinkedList()

    #adding at front:
    ll.push_front(1)
    ll.push_front(2)

    #adding at back:
    ll.push_back(3)
    ll.push_back(4)

    #poping at front:
    #ll.pop_front()

    #poping at back:
    #ll.pop_back()

    #inserting at position:
    ll.insert(3, 8)

    #displaying the linked list nodes!
    ll.display()


print("Above is Nothing but, just a noise")

class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


head = A = LinkedList(1)
B = LinkedList(2)
C = LinkedList(3)
D = LinkedList(4)

A.next = B
B.next = C
C.next = D

def display(head):
    temp = head
    element = []
    while temp:
        element.append(temp.data)
        temp = temp.next

    return element

#remove the 3rd element from the ll.
def remove_ele(val=3):
    i = 1
    temp = head
    while temp is not None and i != val:
        prev = temp
        temp = temp.next
        i += 1

    temp = temp.next
    prev.next = temp


#remove_ele()
#print(display(A))

#display linked list using recursion!
def display_re(head):
    if head is None:
        return 
    print(head.data)
    display_re(head.next)

#reverse the linked list using recursion!
def rev_ll(head):
    prev = None
    nextt = None
    curr = head

    if curr == None:
        head = prev
        return

    nextt = curr.next
    curr.next = prev

    prev = curr
    curr = nextt

    rev_ll(curr)
    



rev_ll(head)
display_re(head)



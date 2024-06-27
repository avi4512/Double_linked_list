class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Double_Linked_list:

    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is Empty...!")
        else:
            temp = self.head
            while temp:
                print(temp.data,'-->',end=" ")
                temp = temp.next


    def before(self,x,data):
        if self.head is None:
            print("No Node is Present")
            return
        if self.head.data == x:
            bn = Node(data)
            bn.next = self.head
            self.head.prev = bn
            self.head = bn
            return

        temp = self.head
        while temp.next:
            if temp.next.data == x:
                break
            else:
                temp = temp.next
        if temp.next is None:
            print("Node not found...")
            return
        na = Node(data)
        na.next = temp.next
        temp.next = na
        na.prev = temp
        temp.next.prev = na







dl = Double_Linked_list()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

dl.head = n1
n1.next = n2
n2.next = n3
n3.next = n4

dl.before(20,15)
dl.before(10,5)
dl.before(40,35)
dl.display()



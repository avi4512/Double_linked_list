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

    def after(self,node,data):

        if self.head is None:
            print("Can't add new Node to without any node!")
            return
        temp = self.head
        while temp:
            if temp.data == node:
                break
            else:
                temp = temp.next
        if temp is None:
            print("Not Found the Node...")
        else:
            na = Node(data)
            na.next = temp.next
            temp.next = na
            na.prev = temp
            temp.next.prev=na



dl = Double_Linked_list()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

dl.head = n1
n1.next = n2
n2.next = n3
n3.next = n4

dl.after(20,25)
dl.after(40,45)
dl.after(10,15)
dl.display()



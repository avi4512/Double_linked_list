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
    def backward(self):
        if self.head is None:
            print("Linked List is Empty...!")

        #to find the last node in the linked list
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            #to print data from the last node
            while temp:
                print(temp.data,'-->',end=" ")
                temp = temp.prev

    def at_pos(self,pos,data):

        if pos == 1:
            np = Node(data)
            np.next = self.head
            np.prev = self.head.prev
            self.head.prev = np
            self.head = np
            return
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next
        np = Node(data)
        np.prev = temp
        np.next = temp.next
        temp.next.prev = np
        temp.next = np


dl = Double_Linked_list()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

dl.head = n1
n1.next = n2
n2.next = n3
n3.next = n4

#prev
n2.prev = n1
n3.prev = n2
n4.prev = n3

dl.at_pos(5,25)


dl.display()
print()
dl.backward()



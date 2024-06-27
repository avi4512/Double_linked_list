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

    def del_end(self):

        if self.head is None:
            print("Can't remove from the Empty linked list..")
            return
        if self.head.next is None:
            self.head = None
            print("Removed Single node and Linked list became Empty")
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.prev.next = None


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


dl.del_end()


dl.display()
print()
dl.backward()



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

    def del_val(self,val):
        #1.Empty
        if self.head is None:
            print("Can't remove from the Empty linked list...!")
            return

        #2.Single Node
        if self.head.next is None:
            if self.head.data == val:
                self.head = None
                print("Dl becoming  Empty..")
                return

        #3.Begining
        if self.head.data == val:
            self.head = self.head.next
            self.head.prev = None
            return

        #4.End
        temp = self.head
        while temp.next:
            if temp.next.data == val:
                break
            else:
                temp = temp.next
        if temp.next is None:
            print("Node Not found..")
        else:
            temp.next = temp.next.next

        #5.Middle
        temp = self.head
        while temp.next is not None:
            if temp.data == val:
                break
            else:
                temp = temp.next

        if temp.next is not None:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev





dl = Double_Linked_list()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

dl.head = n1
n1.next = n2
n2.next = n3
n3.next = n4

n2.prev = n1
n3.prev = n2
n4.prev = n3


dl.del_val(40)


dl.display()
print()
dl.backward()



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


    def begin(self,data):
        if self.head is None:
            nb = Node(data)
            self.head = nb
        else:
            nb = Node(data)
            nb.next = self.head
            self.head.prev = nb
            self.head = nb

d = Double_Linked_list()


d.begin(40)
d.begin(30)
d.begin(20)
d.begin(10)
d.begin(5)


d.display()
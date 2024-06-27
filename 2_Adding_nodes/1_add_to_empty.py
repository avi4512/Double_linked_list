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


    def add_to_empty(self,data):

        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Can't add node because Linked List is NOT Empty..!")

d = Double_Linked_list()

d.add_to_empty(10)
d.add_to_empty(20)
d.display()

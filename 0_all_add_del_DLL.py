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
            print("Empty...")
            return
        temp = self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp = temp.next

    def rev_disp(self):
        if self.head is None:
            print("Empty...")
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data,"-->",end=" ")
            temp = temp.prev



    def at_begin(self,data):

        if self.head is None:
            nb = Node(data)
            self.head = nb
            return
        nb = Node(data)
        nb.next = self.head
        self.head.prev = nb
        self.head = nb

    def at_end(self,data):

        if self.head is None:
            nb = Node(data)
            self.head = nb
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        ne = Node(data)
        ne.prev = temp
        ne.next = temp.next
        temp.next = ne

    def at_pos(self,pos,data):

        if pos == 0:
            np = Node(data)
            np.next = self.head
            self.head.prev = np
            self.head = np
            return

        temp = self.head
        for i in range(pos-1):
            temp = temp.next

        np = Node(data)
        np.prev = temp
        np.next = temp.next
        temp.next.prev  = np
        temp.next = np

    def del_at_begin(self):

        if self.head is None:
            print("Can't Remove from Empty linkedlist..!")
            return

        self.head.next.prev = self.head.prev
        self.head = self.head.next

    def del_at_end(self):
        if self.head is None:
            print("Can't Remove from Empty linkedlist..!")
            return

        temp = self.head
        pre = None
        while temp.next:
            pre = temp
            temp = temp.next
        pre.next = temp.next

    def del_at_pos(self,pos):
        if self.head is None:
            print("Can't Remove from Empty linkedlist..!")
            return
        if pos == 0:
            self.head.next.prev = self.head.prev
            self.head = self.head.next
        temp = self.head

        for i in range(pos-1):
            temp = temp.next
        temp.next.next.prev = temp
        temp.next = temp.next.next

    def del_by_val(self,n):
        if self.head is None:
            print("Can't Remove from Empty linkedlist..!")
            return
        #if val at_begin
        if self.head.data == n:
            self.head.next.prev = self.head.prev
            self.head = self.head.next
            return
        #if val At_end
        temp = self.head
        while temp.next:
            if temp.next.data == n:
                break
            temp = temp.next
        if temp.next is None:
            print("Node Not Found...!")
        else:
            temp.next = temp.next.next
            return 
        #if val in between
        temp = self.head
        pre = None
        while temp:
            if temp.data == n:
                break
            pre = temp
            temp = temp.next
        if temp is None:
            print("Node Not Found...!")
        else:
            temp.next.prev = temp.prev
            pre.next = temp.next





dll = Double_Linked_list()

#Adding
dll.at_begin(30)
dll.at_begin(20)
dll.at_begin(10)
dll.at_end(40)
dll.at_pos(2,25)
dll.at_pos(0,5)

#Deletion
dll.del_at_begin()
dll.del_at_end()
dll.del_at_pos(2)
dll.del_by_val(30)


#display
dll.display()
print()
dll.rev_disp()

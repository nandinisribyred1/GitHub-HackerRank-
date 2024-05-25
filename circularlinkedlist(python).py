class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev1=None

class Circularlinkedlist:
    def __init__(self):
        self.head=None
        self.prev=None

    #-----------Insert at beginning---------#    
    def insertB(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            self.head.next=self.head
        else:
            current=self.head
            while current.next!=self.head:
                current=current.next
            new_node.next = self.head
            current.next=new_node
            self.head = new_node

    #--------Insert at End------------#
    def insertEnd(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next!= self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.head.prev = new_node        # Remove this line also inserts at end

    #-----------Delete at beginning-----------#
    def deleteB(self):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            self.head.prev1.next = self.head.next
            self.head = self.head.next
            self.head.prev1 = self.head.prev1.prev1

    #-----------Display-------------#
    def display(self):
        print(self.head.data,end="->")
        current=self.head.next
        while current!=self.head:
            print(current.data,end="->")
            current=current.next
 #-----------------Find middle element------------#
    def middleElement(self):
        if self.head is None:
            print("List is Empty")
            return
        slow = self.head
        fast = self.head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        print("Middle element is", slow.data)

o=Circularlinkedlist()
print("1.Insert at Beginning")
print("2.Insert at End")
print("3.Delete at Beginning")
print("4.Display")
print("5.Finding the middle element")
while True:
    ch=int(input("Enter your choice:"))
    if ch==1:
        key=int(input("Enter data:"))
        o.insertB(key)
    elif ch==2:
        key=int(input("Enter data:"))
        o.insertEnd(key)
    elif ch==3:
        o.deleteB()
    elif ch==4:
        o.display()
    elif ch==5:
        o.middleElement()
    else:
        exit(0)    
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublelinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    #---------------Insert at Beginning---------------#
    def insertB(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:    
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode  
    #----------------Insert at End-------------------#
    def insertE(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:    
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode    
    #-----------------Insert at certain position--------#
    def insertC(self,data,pos):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        elif pos==1:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
        else:
            c=0
            temp=self.head
            while temp:
                c=c+1
                if c==pos-1:
                    newNode.next=temp.next
                    newNode.prev=temp
                    temp.next=newNode
                    newNode.next.prev=newNode
                temp=temp.next    
            if c<pos-1:
                self.insertE(data)  
    #--------------Delete at front---------------#
    def deleteB(self):
        if self.head is None:
            print("List is Empty")
            return
        elif self.head==self.tail:
            self.head=self.tail=None
        else:    
            self.head=self.head.next
            self.head.prev=None
    #-------------Delete at End-----------------#
    def deleteE(self):
        if self.head is None:
            print("List is Empty")
            return
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head                             #-self.tail-self.tail.prev
            while temp.next!= self.tail:                 #-self.tail.next=None
                temp = temp.next
            temp.next = None
            self.tail = temp           

    #---------------Delete a certain data-----------#
    def deleteC(self,key):
        if self.head is None:
            print("List is Empty")
            return
        elif self.head.next is None:
            self.head = None    
        temp = self.head
        while temp:
            if temp.data == key:
                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                else:
                    self.tail = temp.prev
                return
            temp = temp.next
        print("Key not found")  
          
    #--------------Delete at certain position-----------#
    def deleteP(self, pos):
        if self.head is None:
            print("List is Empty")
            return
        elif self.head.next is None:
            self.head = None    
        temp = self.head
        c=0
        while temp:
            c=c+1
            if c==pos:
                if temp.prev is not None:       
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                else:
                    self.tail = temp.prev
                return
            temp = temp.next  
        print("Key not found")

    #---------------Display from first---------------#
    def Display(self):
        if self.head is None:
            print("List is Empty")
            return
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
    #-----------------Display from back-----------------#    
    def Display1(self):
        if self.head is None:
            print("List is Empty")
            return
        temp=self.tail
        while temp:
            print(temp.data,end="->")
            temp=temp.prev
        print("None")
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
    #------------Minimum----------------------#
    def minimum(self):
        temp=self.head
        if temp is None:
            print("List is Empty")
        else:
            min = temp.data
            current = temp.next
            while current:
                if current.data < min:
                    min = current.data
                current = current.next
        print("Minimum value is", min)
    #---------------Maximum---------------------#
    def maximum(self):
        temp=self.head
        if temp is None:
            print("List is Empty")
        else:
            max = temp.data
            current = temp.next
            while current:
                if current.data > max:
                    max = current.data
                current = current.next
        print("Maximum value is", max)
    #--------------Search--------------------#
    def search(self,key):
        c=0
        temp=self.head
        while temp:
            c=c+1
            if temp.data==key:
                print("Search data is found at ",c)   #print(f"{current.data} is found at {c}")
                break   
            temp=temp.next   
        print("Search element is not found.")
    #--------------Update---------------------#
    def update(self, key, pos):
        if self.head is None:
            self.head = key
        else:
            c = 0
            temp = self.head
            while temp:
                c += 1
                if c == pos :
                    temp.data = key
                    break
                temp = temp.next
            if c < pos:
                self.insertE(key)
#=======================================================================================
ob=DoublelinkedList()
print("1.Insertion at Beginning")
print("2.Insertion at End") 
print("3.Insertion at certain Position")
print("4.Deletion at Beginning")
print("5.Deletion at End")
print("6.Delete a data")
print("7.Delete at certain position")
print("8.Display from front")
print("9.Display from back")
print("10.Finding Middle Element")
print("11.Minimum")
print("12.Maximum")
print("13.Search")
print("14.Update")
while True:
    ch=int(input("Enter your choice:"))
    if ch==1:
        nw=int(input("Enter data:"))
        ob.insertB(nw)
    elif ch==2:
        nw=int(input("Enter data:"))
        ob.insertE(nw)
    elif ch==3:
        nw=int(input("Enter data:"))
        pos=int(input("Enter the position:"))
        ob.insertC(nw,pos)
    elif ch==4:
        ob.deleteB()
    elif ch==5:
        ob.deleteE()  
    elif ch==6:
        nw=int(input("Enter data:"))
        ob.deleteC(nw)
    elif ch==7:
        nw=int(input("Enter position:"))
        ob.deleteP(nw)     
    elif ch==8:
        print("---------Display from front--------")
        ob.Display()
    elif ch==9:
        print("---------Display from back---------")
        ob.Display1()       
    elif ch==10:
        ob.middleElement()  
    elif ch==11:
        ob.minimum()
    elif ch==12:
        ob.maximum() 
    elif ch==13:
        key=int(input("Enter search element:"))
        ob.search(key)  
    elif ch==14:
        key=int(input("Enter data to be updated:"))
        p=int(input("Enter position:"))    
        ob.update(key,p)                     
    else:
        exit(0)

            
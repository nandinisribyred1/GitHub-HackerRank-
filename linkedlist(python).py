class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
    #---------------Insert at Beginning---------------#
    def insertB(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    #---------------Insert at End---------------------#
    def insertE(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newNode
    #---------------Reverse the list---------------------#
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev    
    #---------------Insert at certain position-----------# 
    def insertC(self,data,pos):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            c=0
            temp=self.head
            while temp:
                c=c+1
                if c==pos-1:
                    newNode.next=temp.next
                    temp.next=newNode
                temp=temp.next
            if c<pos-1:
                self.insertE(data)
    #------------Delete at Beginning-------------#            
    def deleteB(self):
        if self.head is None:
            print("List is Empty")
            return
        self.head=self.head.next
    #-------------Delete at End-----------------#
    def deleteE(self):
        if self.head is None:
            print("List is Empty")
            return
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None   
    #--------------Delete a certain data---------#    
    def deleteC(self, key):
        if self.head is None:
            print("List is Empty")
            return
        temp=self.head
        c=0
        while temp:
            if temp.data==key:
                if c==0:
                    self.head=temp.next
                else:
                    prev.next=temp.next
                break
            prev=temp
            temp=temp.next
            c+=1  
    #-----------------Update----------------------#        
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
    #---------------Search------------------#
    def search(self,key):
        c=0
        temp=self.head
        while temp:
            c=c+1
            if temp.data==key:
                print("Search data is found:")
                print(c)   #print(f"{current.data} is found at {c}")
                break   
            temp=temp.next   
        print("Search element is not found.")
    #--------------------Display--------------#
    def Display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
    #----------------Minimum--------------------#
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
    #-------------Finding middle element-----------#
    def middleElement(self):
        if self.head is None:
            print("List is Empty")
            return
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Middle element is", slow.data)   
#=======================================================================
ob=linkedList()
print("1.Insertion at Beginning")
print("2.Insertion at End") 
print("3.Insertion at certain Position")
print("4.Deletion at Beginning")
print("5.Deletion at End")
print("6.Delete a data")
print("7.Display")
print("8.Search")
print("9.Update")
print("10.Reverse")
print("11.Minimum")
print("12.Maximum")
print("13.Finding the middle element")
while True:
    ch=int(input("Enter your choice:"))
    if ch==1:
        nw=int(input("Enter data:"))
        ob.insertB(nw)
    elif ch==2:
        nw=int(input("Enter data:"))
        ob.insertE(nw)
    elif ch==3:
        nw=int(input("Enter data"))
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
        ob.Display()
    elif ch==8:
        nw=int(input("Enter search data:"))
        ob.search(nw)  
    elif ch==9:
        nw=int(input("Enter data:"))
        pos=int(input("Enter position:"))
        ob.update(nw,pos) 
    elif ch==10:
        ob.reverse()   
    elif ch==11:
        ob.minimum()
    elif ch==12:
        ob.maximum()     
    elif ch==13:
        ob.middleElement()             
    else:
        exit(0)





     
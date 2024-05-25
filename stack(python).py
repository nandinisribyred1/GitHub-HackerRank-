class Stack:
    def __init__(self,x):
        self.stack=[]
        self.size=x
        self.top=-1
    def PUSH(self,item):
        if self.top<self.size-1:
            self.stack.append(item)
            self.top += 1
        else:
            print("Stack is Overflow")
    def POP(self):
        if self.top==-1:
            print("Stack is Underflow")
        else:
            self.stack.pop()
            self.top -= 1
    def DISPLAY(self):
        print(self.stack) 


x=int(input("Enter size:"))
ob=Stack(x)
print("1.PUSH")
print("2.POP")
print("3.DISPLAY")
while True:
    nu=int(input(("Enter choice:")))
    if nu==1:
        a=int(input("Enter element to insert:"))
        ob.PUSH(a)
    elif nu==2:
        ob.POP()
    elif nu==3:
        ob.DISPLAY()
    else:
        exit(0)
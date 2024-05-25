class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.rear = self.front = -1

    def ENQUEUE(self, data):
        if self.rear < self.size - 1:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue.append(data)
        else:
            print("Queue is FULL")

    def DISPLAY(self):
        for i in range(self.front, self.rear+1):
            print(self.queue[i], end=" ")
        print()

    def DEQUEUE(self):
        if self.rear == -1 and self.rear<self.front:
            print("Queue is EMPTY")
        else:
            print(self.queue.pop(self.front))
            self.front += 1
            #if self.front > self.rear:
                #self.front = self.rear = -1
size=int(input("Enter size:"))        
q = Queue(size)  
print("1.Insert")
print("2.Delete")
print("3.Display")
while True:
    ch = int(input("Enter choice:"))
    if ch == 1:
        a = int(input("Enter data:"))
        q.ENQUEUE(a)
    elif ch == 2:
        q.DEQUEUE()
    elif ch==3:
        q.DISPLAY()    
    else:
        exit(0)
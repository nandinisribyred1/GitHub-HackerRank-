class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.head = new_node

    # Insert at End
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    # Delete at end
    def delete_end(self):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next.next != self.head:
                current = current.next
            current.next = self.head

    # Display
    def display(self):
        if self.head is None:
            print("List is Empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()

    # Find middle element
    def middle_element(self):
        if self.head is None:
            print("List is Empty")
            return
        slow = self.head
        fast = self.head
        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next
        print("Middle element is", slow.data)

o = CircularLinkedList()
print("1. Insert at Beginning")
print("2. Insert at End")
print("3. Delete at End")
print("4. Display")
print("5. Finding the middle element")
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data: "))
        o.insert_beginning(data)
    elif choice == 2:
        data = int(input("Enter data: "))
        o.insert_end(data)
    elif choice == 3:
        o.delete_end()
    elif choice == 4:
        o.display()
    elif choice == 5:
        o.middle_element()
    else:
        break

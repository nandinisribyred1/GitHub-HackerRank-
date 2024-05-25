class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root=None
    #------------Insertion---------------#    
    def insert(self,key):
        if self.root is None:
            self.root=Node(key)
        else:
            self._insert(key,self.root)
    def _insert(self,key,curr_node):
        if key<curr_node.key:
            if curr_node.left is None:
                curr_node.left=Node(key)
            else:
                self._insert(key,curr_node.left)
        elif key>curr_node.key:
            if curr_node.right is None:
                curr_node.right=Node(key)
            else:
                self.insert(key,curr_node.right)
        return curr_node
    #---------------Inorder-------------#
    def inorder(self):
        if self.root is not None:
            self._inorder(self.root)
    def _inorder(self,curr_node):
        if curr_node is not None:
            self._inorder(curr_node.left)
            print(curr_node.key)
            self._inorder(curr_node.right)
    #-------------PreOrder---------------#
    def preorder(self):
        if self.root is not None:
            self._preorder(self.root)
    def _preorder(self,curr_node):
        if curr_node is not None:
            print(curr_node.key)
            self._preorder(curr_node.left)
            self._preorder(curr_node.right)
    #------------PostOrder----------------#
    def postorder(self):
        if self.root is not None:
            self._postorder(self.root)
    def _postorder(self,curr_node):
        if curr_node is not None:
            self._postorder(curr_node.left)
            self._postorder(curr_node.right) 
            print(curr_node.key)   
    #------------Search----------------------#
    def search(self, key):
        if self.root is not None:
            return self._search(key, self.root, 1)
        else:
            return False

    def _search(self, key, curr_node, pos):
        if curr_node is None:
            print("Search key is not found")
            return False
        elif curr_node.key == key:
            print("Search key is found at position", pos)
            return True
        elif curr_node.key > key:
            return self._search(key, curr_node.left, pos + 1)
        else:
            return self._search(key, curr_node.right, pos + 1)
    #----------------Height-----------------#
    def height(self, key):
        if self.root is not None:
            return self._height(key, self.root, 1)
        else:
            return -1
    def _height(self, key, root, pos):
        if root is None:
            return -1
        elif root.key == key:
            return pos
        elif root.key > key:
            return self._height(key, root.left, pos + 1)
        else:
            return self._height(key, root.right, pos + 1)    
#===================================================================================
obj=BinarySearchTree()
print("1.Insert")
print("2.Inorder")
print("3.Preorder")
print("4.Postorder")
print("5.Search")
print("6.Height")
while True:
    ch=int(input("Enter your choice:"))
    if ch==1:
        key=int(input("Enter the key:"))
        obj.insert(key)
    elif ch==2:
        obj.inorder()
    elif ch==3:
        obj.preorder()
    elif ch==4:
        obj.postorder()
    elif ch==5:
        key=int(input("Enter the search key:"))
        obj.search(key)
    elif ch==6:
        key=int(input("Enter the key:"))
        print("Height of the key is:",obj.height(key))
    else:
        exit(0)    
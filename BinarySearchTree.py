class Node:
    def __init__(self, left=None, data=None, right=None):
        self.left = left
        self.data = data
        self.right = right
class BST:
    def __init__(self, root=None):
        self.root = None

    def is_empty(self):
        return self.root == None

    def insert(self, data):
        new_node = Node(data=data)
        if self.is_empty():
            self.root = new_node
            return  # Inserted the root node, no need for further processing
        temp = self.root
        while temp:
            if data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    break  # Inserted the node, stop traversal
                temp = temp.left
            elif data > temp.data:
                if temp.right is None:
                    temp.right = new_node
                    break  # Inserted the node, stop traversal
                temp = temp.right
            else:
                # Node with the same value exists, handle it as per your requirements
                break
        print("Element Added Successfully")

    # pre oreder traversal
    def preoreder_traversal(self):
        result = []
        self.re_traversal(self.root, result)
        return result

    def re_traversal(self,root, result):
        if root:
            result.append(root.data)
            self.re_traversal(root.left, result)
            self.re_traversal(root.right, result)



    # post order traversal
    def postorder_traversal(self):
        result = []
        self.re_post_traversal(self.root, result)
        return result
    
    def re_post_traversal(self, root, result):
        if root:
            self.re_post_traversal(root.left, result)
            self.re_post_traversal(root.right, result)
            result.append(root.data)

    # inorder traversal
    def inorder_traversal(self):
        result = []
        self.re_inorder_traversal(self.root, result)
        return result

    def re_inorder_traversal(self, root, result):
        if root:
            self.re_inorder_traversal(root.left, result)
            result.append(root.data)
            self.re_inorder_traversal(root.right, result)





        
        



    




def insertBulkElements(arguments, t1):
    for item in arguments:
        t1.insert(item)

t1 = BST()

insertBulkElements([100, 18, 211, 12, 20, 150, 4, 13, 19], t1)



# t1.insert(100)
# t1.insert(18)
# t1.insert(211) 
# t1.insert(12)
# t1.insert(20)
# t1.insert(150)
# t1.insert(4)
# t1.insert(13)
# t1.insert(19)


print(t1.preoreder_traversal())
print(t1.postorder_traversal())
print(t1.inorder_traversal())



print(t1.is_empty())


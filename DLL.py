class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, head=None, tail=None):
        self.head = self.tail = None

    def isEmpty(self):
        if self.head == None and self.tail == None:
            return True

    def addFirst(self, data):
        new_node = Node(None, data, None)
        if self.head == None and self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def addLast(self, data):
        new_node = Node(None, data, None)
        if self.head == None and self.tail == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def search(self, target):
        temp = self.head
        found = False
        while temp:
            if temp.item == target:
                found = True
                return temp
            temp = temp.next
        if found == False:
            return None


    def printList(self):
        temp = self.head
        while temp:
            print(temp.item)
            temp = temp.next

mydll = DLL()
if mydll.isEmpty():
    print("List is empty!")        

mydll.addFirst(10)
mydll.addFirst(20)
mydll.addFirst(30)
mydll.addLast(100)
mydll.addLast(300)
mydll.addFirst(800)
mydll.addAfter(mydll.search(300), 1000)
mydll.printList()
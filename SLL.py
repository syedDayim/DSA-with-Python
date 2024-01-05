class Node():
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL():
    def __init__(self, head=None, tail=None):
        self.head = self.tail = None

    # Checks whether the list is empty or not
    def is_empty(self):
        return self.head is None and self.tail is None

    # Adds a node at the beginning of the list
    def addFirst(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Delete First
    def deleteFirst(self):
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            temp = self.head
            self.head = temp.next
    
    # Adds at the end of the List
    def addLast(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    # Deletes a Node at the End
    def deleteLast(self):
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            temp = self.head
            while True:
                if temp.next == self.tail:
                    temp.next = None
                    self.tail = temp
                    break
                temp = temp.next
    
    
    # Prints the Whole LinkedList
    def showList(self):
        if self.is_empty():
            print("List is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.item, end="=>")
                temp = temp.next
    

myList = SLL()
myList.addFirst(4)
myList.addFirst(5)
myList.addLast(10)
myList.deleteFirst()
myList.deleteFirst()
myList.deleteFirst()
myList.showList()



class Node:
     def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class QueueList:
    def __init__(self, front=None, rear=None):
        self.front = self.rear = None

    def is_empty(self):
        return (self.front is None and self.rear is None)

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

       # Delete First
    def dequeue(self):
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            temp = self.front
            self.front = temp.next

    def get_front(self):
        if self.is_empty():
            return None
        return self.front.data

    def get_rear(self):
        if self.is_empty():
            return None
        return self.rear.data
    
    
    # Prints the Whole LinkedList
    def showList(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            temp = self.front
            while temp is not None:
                print(temp.data, end="=>")
                temp = temp.next
    def getLength(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            count = 0
            temp = self.front
            while temp is not None:
                count += 1
                temp = temp.next
            return count






q = QueueList()
q.enqueue(10)
q.enqueue(20)
q.dequeue()
q.dequeue()

q.showList()

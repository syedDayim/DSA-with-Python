class Queue:
    def __init__(self):
        self.items = []
        self.front = self.rear = None

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, data):
        if len(self.items) == 0:
            self.front = data
        self.items.append(data)
        self.rear = data
        
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        if self.is_empty():
            self.rear = self.front = None

    def get_size(self):
        return len(self.items)

    def get_front(self):
        return self.front

    def get_rear(self):
        return self.rear

    def printQueue(self):
        return self.items



Q1 = Queue()
Q1.enqueue(1)
Q1.enqueue(2)
Q1.enqueue(3)
Q1.enqueue(4)
Q1.enqueue(5)
print(Q1.get_size())

print(Q1.printQueue(), Q1.get_front(), Q1.get_rear())

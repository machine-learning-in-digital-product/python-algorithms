class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return not self.head

    def enqueue(self, new_node):
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            print("Error: Queue is empty")
            return
        
        value = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        return value

    def front(self):
        if self.is_empty():
            print("Error: Queue is empty")
            return
        
        return self.head.value

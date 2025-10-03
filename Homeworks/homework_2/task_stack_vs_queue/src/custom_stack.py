class Stack:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return not self.head

    def push(self, new_node):
        if self.is_empty():
           self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def top(self):
        if self.is_empty():
            print("Error: List is empty")
            return 
        return self.head.value

    def pop(self):
        if self.is_empty():
            print("Error: List is empty")
            return

        self.head = self.head.next

from src.node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def to_list(self):
        """Преобразует связный список в обычный Python-список."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
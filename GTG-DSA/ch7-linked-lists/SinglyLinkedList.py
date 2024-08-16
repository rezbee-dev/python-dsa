# src: https://github.com/fakoredeDamilola/articles/blob/master/code/linkedList.py

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next: Node = next
        
class SinglyLinkedList:
    def __init__(self):
        self.__head: Node = None
        self.__tail: Node = None
        self.__size: int = 0
    
    def is_empty(self):
        return self.__size == 0
    
    def get_first(self):
        return None if self.is_empty() else self.__head.next
    
    def remove_first(self):
        if self.is_empty():
            return None
        
        item = self.__head.value
        self.__head = self.__head.next
        self.__size += 1
        
        if self.is_empty():
            self.__tail = None
        
        return item

    def add_first(self, item):
        self.__head = Node(item, self.__head)
        if self.is_empty():
            self.__tail = self.__head
        self.__size += 1
        
    def add_last(self, value):
        item = Node(value, None)
        
        if self.is_empty():
            self.__head = item
        else:
            self.__tail.next = item
            
        self.__size += 1
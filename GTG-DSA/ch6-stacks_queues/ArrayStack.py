import Empty

# Space: O(n)
# Time: O(1) amortized
# Note: can avoid amortization and ensure O(1) for all operations if maximum capacity is set
class ArrayStack:
    """LIFO Stack implementation using Python list as underlying storage"""
    
    def __init__(self):
        self._data = []
        
    # O(1)
    def __len__(self):
        return len(self._data)
    
    # O(1)
    def is_empty(self):
        return len(self._data) == 0
    
    # O(1) amortized
    def push(self, e):
        self._data.append(e)
        
    # O(1)
    def top(self):
        """Return (do not remove) element at the top of the stack
           Raise Empty Exception if stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        
        return self._data[-1]
        
    # O(1) amortized
    def pop(self):
        """Remove and return the element from the top of the stack (LIFO).
           Raise Empty Exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        
        return self.data.pop()
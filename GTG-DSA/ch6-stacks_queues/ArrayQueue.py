import Empty
 
class ArrayQueue:
    """FIFO queue implementation using python List"""
    
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        # initialize empty queue with nulls
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0 # Actual number of elements in queue
        self._front = 0 # front = beginning = first element to be dequeued
        
    def __len__(self):
        # not using len() since that is the CAPACITY, not the actual number of elements
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue. 
           Raise Empty exception if queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]
    
    def dequeue(self):
        """
            Remove and return the first element of the queue
            Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        
        return answer
    
    def enqueue(self, e):
        """Add an element to the back of the queue"""
        
        # Double the size if capacity is reached
        if self._size == len(self._data):
            self._resize()
            
        # Next free spot for new element (aka back of the queue)
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        
def _resize(self):
    """Resize to a new list of greater capacity"""
    # Current list
    old = self._data
    # Resize list to bigger capacity, and initialize to None
    self._data = [None] * (2 * len(self.data))
    
    # index for traversing old list
    walk = self._front
    for k in range(self._size):
        self._data[k] = old[walk]
        # shift index frontward, while maintaining circularity
        walk = (1+walk) % len(old)
        
    self._front = 0
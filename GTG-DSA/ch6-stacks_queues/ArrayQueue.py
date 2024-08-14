import Empty
 
# Space: O(n)
class ArrayQueue:
    """FIFO queue implementation using python List"""
    
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        # initialize empty queue with nulls
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0 # Actual number of elements in queue
        self._front = 0 # front = beginning = first element to be dequeued
        
    # O(1)        
    def __len__(self):
        # not using len() since that is the CAPACITY, not the actual number of elements
        return self._size
    
    # O(1)
    def is_empty(self):
        return self._size == 0
    
    # O(1)
    def first(self):
        """Return (but do not remove) the element at the front of the queue. 
           Raise Empty exception if queue is empty
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]
    
    # O(1) amortized
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
        
        # shrink list
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        
        return answer
    
    # O(1)amortized
    def enqueue(self, e):
        """Add an element to the back of the queue"""
        
        # Double the size if capacity is reached
        if self._size == len(self._data):
            self._resize(2 * len(self.data))
            
        # Next free spot for new element (aka back of the queue)
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        
    # O(n) (?)
    def _resize(self, cap):
        """Resize to a new list of greater capacity"""
        # Current list
        old = self._data
        # Resize list to bigger capacity, and initialize to None
        self._data = [None] * cap
        
        # index for traversing old list
        walk = self._front
        # See assets/gtg-6_7-queue_resizing.png
        # We need to realign indices of the old list to be starting at 0 in the new list
        for k in range(self._size):
            self._data[k] = old[walk]
            # shift index frontward, while maintaining circularity
            walk = (1+walk) % len(old)
            
        self._front = 0
import ctypes

# pg 196
# 
class DynamicArray:
    """A dynamic array class"""
    
    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._arr = self._create_arr(self._capacity)
        
    def _create_arr(self, c):
        # see: https://docs.python.org/3/c-api/structures.html#c.PyObject
        # create pointer to array of objects of type PyObject, and instantiate it (see the '()' at the end)
        # This allows us to create an array of generic python objects
        return (c * ctypes.py_object)()
    
    def _resize(self):
        # create new array with size = self._capacity * 2
        # for i in old arry, new_arry[i] = old_arr[i]
        
        self._capacity = self._capacity * 2
        new_arr = self._create_arr(self._capacity)
        
        for i in range(self._size):
            new_arr[i] = self._arr[i]
            
        self._arr = new_arr
        
    def __len__(self):
        return self._size
    
    def __get_item__(self, k):
        if not 0 <= k < self.size:
            raise IndexError("Invalid Array Index")
    
    # O(n) (amortized)
    def append(self, item):
        if self.size == self._capacity:
            self._resize() # double the array
            
        self._arr[self._size] = item
        self._size += 1
        
    # O(n-k+1) (amortized)
    # Insert item and shift elements rightward if appropriate
    def insert(self, target_index, value):
        # we assume 0 <= target_index <= size
        
        if self._size == self._capacity:
            self._resize()
        
        # Start at end of list and traverse backwards to target_index
        #   shifting elements rightward until reaching target_index
        for current_index in range(self._size, target_index, -1):    
            self._arr[current_index] = self._arr[current_index-1]
            
        self._arr[target_index] = value
        self._size += 1
        
    # O(n)
    def remove(self, value):
        """Remove first ocurrence of value or raise ValueError if not exists"""
        # Todo: implement array shrinking
        
        for k in range(self._size):
            if self._arr[k] == value:
                # shift elements leftward
                for j in range(k, self._size-1):
                    self._arr[j] = self._arr[j+1]
                    
                self._arr[self._size - 1] = None # garbage collection
                self._size -= 1
                return # exit
        
        raise ValueError("value not found")
        
# Todo: test DynamicArray class for errors and functionality
# Todo: include functionality to shrink array size whenever the actual size falls below a threshold (see pg 200)
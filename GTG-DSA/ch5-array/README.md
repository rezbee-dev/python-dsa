# CH5 - Array-Based Sequences

Memory Address
- What is Memory Address?
  - Unique number associated with a byte in computer memory (RAM?)
- How are Memory addresses represented?
  - Binary Number, represented in Hex format, ex: `0x7FFF5FBFFD98`
- How many bits in a byte?
  - 8 bits
- How are memory addresses "laid out"? How do the memory addresses relate to each other?
  - Addresses are in sequential order, like an array

Arrays
- How is the size of the cells in an array determined?
  - Determined by the type of data being stored
  - ex: strings are stored as characters, with each character being represented as Unicode, and thus requireing 16bits/2bytes
- Can array cell sizes differ from each other?
  - No, each cell of an array must use the same number of bytes
- How are the cells in an array accessed? How is the memory address of an array cell calculated? (* pointers)
  - Array Cell Memory Address = (Memory address at Index 0) + cellsize * index

Referential Arrays
- Given that array cells must use the same amount of memory, how is data of differing sizes stored? ex: strings of varying lengths?
  - Ex: ` [ Rene , Joseph , Janet , Jonas , Helen , Virginia , ... ]`
  - Arrays store "references" or "memory addresses", that point to the actual "values"
  - References are of constant size, so you can "store" values of any size in an array by storing its address in memory
- Which type of array requires higher memory usage, arrays of memory addresses or arrays of primitives?
  - In python, arrays that store memory addresses require more higher memory usage, as they allocate 64bits for storing memory addresses, regardless of the actual size of the datatype stored
- How are elements in Reference arrays stored?
  - Memory addresses are stored sequentially in the array, but the elements the memory points to reside randomly in the heap

Dynamic Arrays
- Given that arrays must be of a fixed length, how are Lists used without having a fixed size?
  - The underlying data structue of a List has a greater capacity than its current length, that allows elements to be inserted without being full
  - When the available capacity is exhausted, a new, larger array is created and contents from the current array is copied over
- Whats more performant when combining arrays: `extend()` method that adds another array to the original array, or calling `append()` multiple times for each element in the array to be copied over?
  - `extend()` method is more performant:
    - in list, tuple, etc, `extend()` method may feature optimizations via native implemenations (?)
    - less overhead to a single function call verses many individual function calls
    - resulting size of the `append` operation can be calculated in advance
      - and with multiple `append`, you may end up resizing more than once
- Whats more performant, list comprehensions or for loops?
  - List comprehensions, see: https://switowski.com/blog/for-loop-vs-list-comprehension/

Amortized Analysis
- What is amortized analysis?
  - technique for estimating the run-time cost over a sequence of operations
  - it attempts to average out the worst operations out over time, to provide a more accurate picture of performance
    - for example, a data structure has one costly operation, but it doesn't get performed very often. It's not accurate to say the DS is inefficient because of that one costly operation
  - Ex: Dynamic Arrays, `append` operations are normally efficient until it needs to be resized. If we sum up all the "costs", it would be O(n^2), but this is overly pessimistic. On average, it is O(n) (with amortized analysis)
    - the amount "saved" during normal, efficient `append` operations makes up for the costly resizing operation
- What is the performance difference between resizing array via fixed increments and doubling the array?
  - Fixed increments: O(n^2)
  - Doubling (or increasing by some factor): O(n)
- Note: We need to account for shrinking the array too
  - Array will lose O(n) performance in storage and time if data is frequently resized but not shrank when data is removed

Strings
- What is the time complexity for concatenating Strings in an iteration?
  - O(n^2)
  - Why? -> https://www.reddit.com/r/learnprogramming/comments/4uh2b6/java_how_is_the_running_time_of_string/
  - Strings are immutable (unchanging), therefore a new String is created rather than being modified
  - The operation in concatenating strings is: Creating new string, copying the characters of each string over to new string
- Why would langauges make Strings immutable?
  - _Note: mainly applies to Java_; see https://stackoverflow.com/a/22398067
  - Security: if other objects refer to it, then changing the string may case bugs or unexpected behavior (connection URLs, passwords, etc)
  - Synchronization: Makes it thread safe, solving thread sync issues
  - Caching: If a string already exists in string pool, then a new one does not need to be created
- How do you concatenate Strings, in an efficient way?
  - Python: using `"".join(tempArr)`
  - Java: using StringBuilder
  - The basic idea is to create a resizable array to push the strings into, and then only creating a final string at the end, instead of multiple times

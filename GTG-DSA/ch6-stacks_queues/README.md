# CH6 - Stacks, Queues, and Dequeues

## Stacks

In which manner are objects inserted/ removed from stack?
- LIFO (last-in, last-out)
- Elements are added on "top" of the stack, and removed from the top of the stack

What are some usecases of stacks (or LIFO)?
- Anytime you need to access the most recent item in a sequence
- Anytime you need to use sequence in reverse order
- "Back" button in web browsers (returns most recent page)
- "Undo" mechanism in text editors (cancels most recent text change)
- "Balanced Parenthesis" where code editor checks if parenthesis are closed properly
- Storing function calls
- Reversing word (push a word onto a stack, and pop it to get letters in reversed order)
- Depth First Search
- Expression evaluation (ex: arithmetic expressions)

## Queues

In which manner are objects inserted/removed from queue?
- FIFO (first-in, first-out)
- Elements enter from one end and are removed from the opposite end

What are some usecases of queues (or FIFO)?
- Anytime you need to access the oldest item in a sequence
- Managing requests, where the oldest request is handled first
  - Web servers, traffic
  - CPU/ Disk scheduled tasks
  - Routers and switches in networking (packet queueing)
- Printer Spooler
  - where documents are queued up for printing
  - the oldest added document is printed first

(Python specific) Why not use the same approach as in the Stack class implementation where List is used for the underlying data structure for Queue implementation?
- It is inefficient due to requiring elements to be shifted, O(n)
  - Since elements are inserted and removed on opposite ends of the data structure, it may result in shifting of elements if element is inserted/removed from the beginning of the list

(Python Specific) What approach is used when implementing Queue with Lists?
- Using List "circularly"
  - Queue will maintain index of the "first" element (aka "front index")
  - When element is dequeued, the "front index" is shifted rightwards
  - the new index is calculated with this formula: `(current_front_index + 1) % num_of_elements_in_queue`


## Double-Ended Queues

What is the difference between Queue and Deque (pronounced "deck")?
- Queue only supports insertion and deletion from _one end_
- Deque supports insertion and deletion from _both ends_

What are some use-cases of Deque
- Used for performing clockwise, anti-clockwise operations in O(1)
- Can be used to implement Stack and Queue  (?)
- BFS algorithm
- To manage the order & priority of items (ex: tickets, requests, etc)
  - Items can be added to the front or back of the queue depending on priority or deadline

_Todo_: Need to implement Deque in python, see p 248
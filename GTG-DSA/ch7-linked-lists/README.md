# CH7 - Linked List

What are the disadvantages of Arrays?
- The length the array (capacity) might be substantially bigger than the actual number of elements that it stores
  - i.e unoptimal memory allocation
- Insertions and deletions can be very expensive
- Must be resized due to fixed lengths

## Singly Linked Lists

What is a Singly Linked List?
- collection of nodes that collectively form a linear sequence

What does a node consist of (in a Singly Linked List)?
- Reference to the actual data that is the element of the sequence
- Reference to the next node of the Singly Linked List

## Doubly Linked List

What is doubly linked lists?
- Similiar to Singly Linked List except its nodes also contains a reference to the _previous_ node

What does the "previous" node allow us to do in a Doubly Linked List?
- Allows for bidirectional traversal 
- Allows for efficient deletion of a node at the tail of the list
- Allows for insertions/ deletions at arbitrary positions within the list

What are sentinel nodes?
- AKA guards
- Dummy nodes placed at head and tail of linked list that does not store elements of the primary sequence, whose purpose is to simplify the logic of linked list operations and eliminate any "special cases" (ex: empty lists)

## Positional List

What is the motivation behind Positional Lists? (pg 277)
- Linked lists without positions don't allow for easy arbitrary insertions and deletions and don't allow user to refer to elements anywhere in the sequence

Why are (numeric) indices not a good choice for describing positions/locations within a linked list?
- Not efficient
  - even knowing index, you still have to traverse the list to reach it
- Numeric indicies changes over time due to insertions/deletions

Why are nodes good at describing a position in list, yet not the recommended way to implement positions?
- You can perform O(1)-time insertions and deletions at arbitrary positions of the list if given a reference to the relevent node
  - this is because, the node itself contains pointers to the previous and next nodes
- However, its not good idea to directly use nodes as positions since it violates encapsulation

What is a `position` data type? (p279)
- a marker or token that describes a location/ position in a linked list, for navigation

Is `position` affected by insertions/deletions in linked list?
- No

How does `position` become invalid?
- by issuing explicit command to delete it

## Link-based vs Array-based Sequences

What are the advantages of array-based sequences?
- O(1)-time access to any element via index
  - O(k)-time to locate kth element in Singly Linked List
  - O(n-k) time to locate element if traversing backwards from end of doubly linked list
- More efficency for equivalent Array and Linked List operations
  - because unlike arrays, with linked list you may have to instantiate nodes (objects)
- Less memory usage (proportionally)
  - although arrays involve extra memory usage due to resizing, linked lists involve more memory since each node stores references to previous and next nodes

What are the advantages of linked-based sequences?
- Consistent run-time for operations
  - unlike arrays that have amortized-bound runtimes due to resizing
    - this is a disadvantage for real-time applications since you woudn't want a delay/interruption due to a resizing event
- Support for O(1)-time insertions/deletions at arbitrary positions
  - unlike arrays where each insertion/deletion involves shifting of elements and potentially a resize event

## Skipped (to be noted later)
- Stack w/singly linked list implementation
- Queue w/singly linked list implementation
- Queue w/circularly linked list implementation
- Round-robin schedulers 
- Doubly Linked List implementation
- Deque w/doubly linked list implementation
- PositionalList w/doublylinkedlist implementation
  - sorting positional list (p285)
- Case study: Maintaining access frequences (p 286)
  - Move-to-front heuristic
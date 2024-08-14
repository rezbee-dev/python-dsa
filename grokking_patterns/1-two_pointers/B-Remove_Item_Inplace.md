# Remove Instances of Target in Array

*Similiar to Find Non-Duplicate Number Instances (easy)*

## Problem
Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

Example 1:

- Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
- Output: 4
- Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].

Example 2:

- Input: [2, 11, 2, 2, 1], Key=2
- Output: 2
- Explanation: The first two elements after removing every 'Key' will be [11, 1].

## Solution


```py
# Time Complexity: O(n)
# Space Complexity: O(1) 
class Solution:
  def remove(self, arr, key):
    nextElement = 0  # Initialize a variable to keep track of the next non-'key' element index.
    
    # Iterate through the input array 'arr'.
    for i in range(len(arr)):
      if arr[i] != key:  # Check if the current element is not equal to 'key'.
        arr[nextElement] = arr[i]  # If not equal, copy the current element to the next available position.
        nextElement += 1  # Increment the nextElement index to prepare for the next non-'key' element.

    return nextElement  # Return the length of the modified array, which represents the new length.


def main():
  sol = Solution()
  
  # Test case 1
  print("Array new length: " + str(sol.remove([3, 2, 3, 6, 3, 10, 9, 3], 3))) # Expected 4
  
  # Test case 2
  print("Array new length: " + str(sol.remove([2, 11, 2, 2, 1], 2))) # Expected 2

main()
```
# Sqrt

## Problem Statement
- Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be non-negative as well.
- You must not use any built-in exponent function or operator.
- For example, do not use `pow(x, 0.5)` in c++ or `x ** 0.5` in python.

Example 1:

- Input: x = 8
- Output: 2
- Explanation: The square root of 8 is 2.8284, and since we need to return the floor of the square root (integer), hence we returned 2.  

Example 2:

- Input: x = 4
- Output: 2
- Explanation: The square root of 4 is 2.

Example 3:

- Input: x = 2
- Output: 1
- Explanation: The square root of 2 is 1.414, and since we need to return the floor of the square root (integer), hence we returned 1.  

Constraints:

- 0 <= `x` <= 2^31 - 1

## Solution

- We can use a Binary Search approach to calculate the square root of an integer x without using any in-built sqrt function.
- For any integer x, the square root of x will lie between 0 and x/2 (inclusive) for x > 2. 
- Therefore, we can efficiently use binary search within this range to find the integer part of the square root (i.e., the floor value). 
- By narrowing down the potential values step-by-step, binary search allows us to determine the largest integer y such that y*y is less than or equal to x.
- This approach ensures an efficient and accurate computation of the square root, especially for large values of x, due to the logarithmic nature of binary search.

**Step-by-Step Algorithm**
1. Handle Base Cases: If `x` is less than 2, return `x` directly 
   - since the square root of 0 is 0, and the square root of 1 is 1
2. Initialize Pointers: Set left to 2 and right to `x` / 2.
3. Binary Search Loop:
   - While `left` is less than or equal to `right`:
     - Calculate `mid` as `left + (right - left) // 2`.
     - Calculate `num` as `mid * mid`.
     - If `num` is greater than `x`, move `right` to `mid - 1`.
     - If `num` is less than `x`, move `left` to `mid + 1`.
     - If `num` equals `x`, return mid.
4. Return Result: Return right as the integer part of the square root of `x`.


```py
import math

class Solution:
  def mySqrt(self, x: int) -> int:
    if x < 2:
      return x # return x if it is 0 or 1

    left, right = 2, x // 2 
    mid = 0
    num = 0 
    while left <= right: # binary search for the square root
      mid = left + (right - left) // 2 # find the middle element
      num = mid * mid
      if num > x:
        right = mid - 1 # if mid * mid is greater than x, set right to mid - 1
      elif num < x:
        left = mid + 1 # if mid * mid is less than x, set left to mid + 1
      else:
        return mid # if mid * mid is equal to x, return mid
    return right

solution = Solution()

input1 = 4
expectedOutput1 = 2
result1 = solution.mySqrt(input1)
print(result1 == expectedOutput1) # Expected output: True

input2 = 8
expectedOutput2 = 2
result2 = solution.mySqrt(input2)
print(result2 == expectedOutput2) # Expected output: True

input4 = 2
expectedOutput4 = 1
result4 = solution.mySqrt(input4)
print(result4 == expectedOutput4) # Expected output: True

input5 = 3
expectedOutput5 = 1
result5 = solution.mySqrt(input5)
print(result5 == expectedOutput5) # Expected output: True

input6 = 15
expectedOutput6 = 3
result6 = solution.mySqrt(input6)
print(result6 == expectedOutput6) # Expected output: True
```
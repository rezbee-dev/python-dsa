# Number of Good Pairs

## Problem Statement
- Given an array of integers `nums`, return the number of good pairs.
- A pair (i, j) is called good if `nums[i] == nums[j]` and `i < j`.

Example 1:

- Input: nums = [1,2,3,1,1,3]
- Output: 4
- Explanation: There are 4 good pairs, here are the indices: (0,3), (0,4), (3,4), (2,5).

Example 2:

- Input: nums = [1,1,1,1]
- Output: 6
- Explanation: Each pair in the array is a 'good pair'.

Example 3:

- Input: words = nums = [1,2,3]
- Output: 0
- Explanation: No number is repeating.

Constraints:

- 1 <= `nums.length` <= 100
- 1 <= `nums[i]` <= 100

## Solution

- We can use a HashMap to store the frequency of each number in the input array `nums`

- While iterating through the input array, for each number `n` in the array, we will increment the count of `n` in the HashMap.

- Whenever we find a new occurrence of a number, we have found a new pair.

- Every new occurrence of a number can be paired with every previous occurrence of the same number. This means if a number has already appeared `p` times, we will have `p-1` new pairs.

- Hence, whenever we find a new occurrence of a number (that is, its count is more than 1), we will add `p-1` to `pairCount`, which keeps track of the total number of good pairs.

```py
# Time and Space Complexity: O(n)
class Solution:
  def numGoodPairs(self, nums):
    pairCount = 0
    map = {}
    for n in nums:
      map[n] = map.get(n, 0) + 1 # increment the count of 'n' in the map
      # every new occurrence of a number can be paired with every previous occurrence
      # so if a number has already appeared 'p' times, we will have 'p-1' new pairs
      pairCount += map[n] - 1
    return pairCount

if __name__ == '__main__':
  sol = Solution()
  nums1 = [1, 2, 3, 1, 1, 3]
  result1 = sol.numGoodPairs(nums1)
  print("Result 1:", result1, "(Expected: 4)")

  nums2 = [1, 1, 1, 1]
  result2 = sol.numGoodPairs(nums2)
  print("Result 2:", result2, "(Expected: 6)")

  nums3 = [1, 2, 3]
  result3 = sol.numGoodPairs(nums3)
  print("Result 3:", result3, "(Expected: 0)")
```
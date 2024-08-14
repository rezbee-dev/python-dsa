# Valid Anagram

## Problem Statement

- Given two strings `s`and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
- An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

- Input: s = "listen", t = "silent"
- Output: true

Example 2:

- Input: s = "rat", t = "car"
- Output: false

Example 3:

- Input: s = "hello", t = "world"
- Output: false

Constraints:

- 1 <= `s.length`, `t.length` <= 5 * 10^4
- `s` and `t` consist of lowercase English letters.

## Solution
- We can solve this problem by calculating how many times each character appears in both the strings. 
- If the frequency of each character is the same in both the given strings, we can conclude that the strings are anagrams of each other.
- We can use a hash map to store the frequency of each character in both strings.
- For each character in the string, the frequency of that character in string `s` is incremented and the frequency of that character in string `t` is decremented. 
  - After iterating over all characters in the strings, we will check if the frequency of all characters is 0. 
  - If it is, the strings are anagrams of each other and the function returns `true`. Otherwise, it returns `false`

```py
# Time: O(n)
# Space: O(k) or O(1)
class Solution:
  def isAnagram(self, s, t):
    # Check if the lengths of both strings are equal. If not, return false.
    if len(s) != len(t):
      return False

    # Create a hash map to store the frequency of characters in both strings.
    freq_map = {}
    for i in range(len(s)):
      # Increment the frequency of the character in string s.
      if s[i] in freq_map:
        freq_map[s[i]] += 1
      else:
        freq_map[s[i]] = 1

      # Decrement the frequency of the character in string t.
      if t[i] in freq_map:
        freq_map[t[i]] -= 1
      else:
        freq_map[t[i]] = -1

    # Check if the frequency of all characters is 0.
    for char in freq_map:
      if freq_map[char] != 0:
        return False

    # If all characters have a frequency of 0, this means that 't' is an anagram of 's'.
    return True

sol = Solution()
# Test case 1
s1 = "listen"
t1 = "silent"
print(sol.isAnagram(s1, t1))  # Expected output: True

# Test case 2
s2 = "hello"
t2 = "world"
print(sol.isAnagram(s2, t2))  # Expected output: False

# Test case 3
s3 = "anagram"
t3 = "nagaram"
print(sol.isAnagram(s3, t3))  # Expected output: True

# Test case 4
s4 = "rat"
t4 = "car"
print(sol.isAnagram(s4, t4))  # Expected output: False

# Test case 5
s5 = ""
t5 = ""
print(sol.isAnagram(s5, t5))  # Expected output: True
```
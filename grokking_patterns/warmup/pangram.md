# Pangram

## Problem Statement
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing English letters (lower or upper-case), return `true` if sentence is a pangram, or `false` otherwise.

Note: The given sentence might contain other characters like digits or spaces, your solution should handle these too.

*Example 1:*
```
Input: sentence = "TheQuickBrownFoxJumpsOverTheLazyDog"
Output: true
Explanation: The sentence contains at least one occurrence of every letter of the English alphabet either in lower or upper case.
```

*Example 2:*
```
Input: sentence = "This is not a pangram"
Output: false
Explanation: The sentence doesn't contain at least one occurrence of every letter of the English alphabet.
```

*Constraints:*
- 1 <= sentence.length <= 1000
- sentence consists of lower or upper-case English letters

## Solution
- We can use a HashSet to check if the given sentence is a pangram or not. 
- The HashSet will be used to store all the unique characters in the sentence. 
- The algorithm works as follows:
  - Converts the sentence to lowercase.
  - Iterate over each character of the sentence using a loop.
  - Add each character to the HashSet.
  - After looping through all characters, compare the size of the HashSet with 26 (total number of alphabets). 
    - If the size of the HashSet is equal to 26, it means the sentence contains all the alphabets and is a pangram, so the function will return true. 
    - Otherwise, it will return false.

```py
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
  def checkIfPangram(self, sentence):
    seen = set() # Create a set to store unique characters

    # Convert sentence to lowercase and iterate over each character
    for currChar in sentence.lower():
      if currChar.isalpha():
        seen.add(currChar) # Add the character to set

    # Return true if set size is 26 (total number of alphabets)
    return len(seen) == 26

# Test cases
sol = Solution()
# Test case 1: "TheQuickBrownFoxJumpsOverTheLazyDog"
# Expected output: True
print(sol.checkIfPangram("TheQuickBrownFoxJumpsOverTheLazyDog"))

# Test case 2: "This is not a pangram"
# Expected output: False
print(sol.checkIfPangram("This is not a pangram"))

# Test case 3: "abcdef ghijkl mnopqr stuvwxyz"
# Expected output: True
print(sol.checkIfPangram("abcdef ghijkl mnopqr stuvwxyz"))

# Test case 4: ""
# Expected output: False
print(sol.checkIfPangram(""))

# Test case 5: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Expected output: True
print(sol.checkIfPangram("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
```
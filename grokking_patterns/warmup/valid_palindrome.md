# Valid Palindrome

## Problem Statement

- A phrase is a palindrome if it reads the same forward and backward
  - after converting all uppercase letters into lowercase letters
  - after removing all non-alphanumeric characters
- Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

Example 1:

- Input: sentence = "A man, a plan, a canal, Panama!"
- Output: true
- Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

- Input: sentence = "Was it a car or a cat I saw?"
- Output: true
- Explanation: Explanation: "wasitacaroracatisaw" is a palindrome.

Example 3:

- Input: sentence = "race a car"
- Output: false
- Explanation: Explanation: "raceacar" is not a palindrome.

Constraints:

- 1 <= s.length <= 2 * 10^5
- `s` consists only of printable ASCII characters.

## Solution

This problem aims to check if a given string is a palindrome. 

A palindrome is a word, phrase, number, or other sequences of characters that read the same forward and backward, ignoring spaces, punctuation, and capitalization. 

Our algorithm can leverage the two-pointer technique where one pointer starts at the beginning of the string, and the other one starts at the end. 

The two pointers move towards each other, checking if the characters they point to are the same.

**Walkthrough of the algorithm**

1. The `isPalindrome` function starts by setting two pointers: 'i' at the start of the string and 'j' at the end.

2. Then it enters a while loop which continues until the two pointers cross each other. Inside this loop:
   - The first inner while loop moves 'i' forward, skipping any characters that are not letters or digits, until it points to a valid character or it crosses 'j'.
   - The second inner while loop moves 'j' backward, skipping any characters that are not letters or digits, until it points to a valid character or it crosses 'i'.

3. After finding valid characters at 'i' and 'j', it converts these characters to lowercase and checks if they're the same.
   - If they're not the same, the function immediately returns false since the string can't be a palindrome if these characters are different.
   - If they are the same, 'i' is incremented and 'j' is decremented, and the loop continues to the next pair of characters.

4. If the while loop completes without finding any unequal pairs of characters, the function returns true, indicating that the string is a palindrome.

```py
# Time: O(n)
# Space: O(1)
class Solution:
  def isPalindrome(self, s: str) -> bool:
    i, j = 0, len(s) - 1 # initialize two pointers, one at the start and one at the end of the string
    
    while i < j: # continue until the two pointers cross over
      while i < j and not s[i].isalnum(): # move i forward until a letter or digit is found
        i += 1
      while i < j and not s[j].isalnum(): # move j backward until a letter or digit is found
        j -= 1
          
      # compare the characters at i and j after converting them to lowercase
      if s[i].lower() != s[j].lower(): 
        return False # if they are not equal, the string is not a palindrome
      i += 1 # move i forward
      j -= 1 # move j backwards
        
    return True # if the two pointers have crossed over, the string is a palindrome

if __name__ == "__main__":
  sol = Solution()
  # Test case 1: "A man, a plan, a canal, Panama!"
  # Expected output: True
  print(sol.isPalindrome("A man, a plan, a canal, Panama!"))

  # Test case 2: "race a car"
  # Expected output: False
  print(sol.isPalindrome("race a car"))

  # Test case 3: "Was it a car or a cat I saw?"
  # Expected output: True
  print(sol.isPalindrome("Was it a car or a cat I saw?"))

  # Test case 4: "Madam, in Eden, I'm Adam."
  # Expected output: True
  print(sol.isPalindrome("Madam, in Eden, I'm Adam."))

  # Test case 5: "empty string"
  # Expected output: True
  print(sol.isPalindrome(""))

```
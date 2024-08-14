# Reverse Vowels

## Problem Statement
Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

*Example 1:*

- Input: `s= "hello"`
- Output: `"holle"`


*Example 2:*

- Input: `s= "AEIOU"`
- Output: `"UOIEA"`


*Example 3:*

- Input: `s= "DesignGUrus"`
- Output: `"DusUgnGires"`


*Constraints:*
- 1 <= `s.length` <= 3 * 10^5
- `s` consist of printable ASCII characters

## Solution

- We need to reverse the vowels in a string, keeping the positions of the consonants and other characters intact. 
- We can use the two-pointer technique to traverse the string from both ends simultaneously. 
- Whenever a vowel is encountered at both ends, we will swap them. 
- The process will continue until the two pointers meet in the middle.

Walk through of the algorithm
1. We first create a static string "vowels" that contains all lowercase and uppercase vowels. 
    - This is used for checking whether a character in the input string is a vowel.
2. The `reverseVowels` method accepts a string 's' as an argument. 
    - The first and last pointers are initialized to the start and end of the string, respectively.
3. We convert the input string 's' to a character array 'array' to allow easy manipulation of individual characters.
4. We enter a while loop that continues while 'first' is less than 'last'.
5. Inside the while loop, we have two nested while loops:
    - The first nested while loop keeps incrementing the 'first' pointer until it points to a vowel or 'first' is no longer less than 'last'.
    - The second nested while loop keeps decrementing the 'last' pointer until it points to a vowel or 'first' is no longer less than 'last'.
6. Once we've found a vowel at both the 'first' and 'last' pointers, we swap these vowels.
7. After the swap, we increment the 'first' pointer and decrement the 'last' pointer, and continue to the next iteration of the outer while loop.
8. After exiting the while loop, we convert the character array back to a string and return it as the result.

```py
# time complexity: O(n)
# space complexity: O(n)
class Solution:
  vowels = "aeiouAEIOU"

  def reverseVowels(self, s: str) -> str:
    # initialize pointers for start and end of the string
    first, last = 0, len(s) - 1
    array = list(s)
    while first < last:
      # increment the start pointer until a vowel is found
      # str.find() returns -1 if not found
      while first < last and self.vowels.find(array[first]) == -1:
        first += 1
      # decrement the end pointer until a vowel is found
      while first < last and self.vowels.find(array[last]) == -1:
        last -= 1
      # swap the values of first and last if both are vowels
      array[first], array[last] = array[last], array[first]
      # move the pointers towards the center
      first += 1
      last -= 1

    # return the modified string
    return "".join(array)
    

if __name__ == "__main__":
  solution = Solution()

  s1 = "hello"
  expected_output1 = "holle"
  actual_output1 = solution.reverseVowels(s1)
  print("Test Case 1: ", expected_output1 == actual_output1)

  s2 = "DesignGUrus"
  expected_output2 = "DusUgnGires"
  actual_output2 = solution.reverseVowels(s2)
  print("Test Case 2: ", expected_output2 == actual_output2)

  s3 = "AEIOU"
  expected_output3 = "UOIEA"
  actual_output3 = solution.reverseVowels(s3)
  print("Test Case 3: ", expected_output3 == actual_output3)

  s4 = "aA"
  expected_output4 = "Aa"
  actual_output4 = solution.reverseVowels(s4)
  print("Test Case 4: ", expected_output4 == actual_output4)

  s5 = ""
  expected_output5 = ""
  actual_output5 = solution.reverseVowels(s5)
  print("Test Case 5: ", expected_output5 == actual_output5)
```
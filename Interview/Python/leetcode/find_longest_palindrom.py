#Write a Python function called find_longest_palindrome that takes a string as input and returns the longest palindromic substring in the string.

#A palindromic string is a string that is spelled the same forwards and backwards, e.g. "racecar". A substring is a contiguous sequence of characters within a string.


from typing import List

def find_longest_palindrome(string):
  # Edge case: empty input
  if not string:
    return ""

  # Initialize the longest palindrome to the first character
  longest_palindrome = string[0]

  # Iterate through each character in the string
  for i in range(len(string)):
    # Check for palindromes of odd length centered at this character
    palindrome = find_palindrome(string, i, i)
    if len(palindrome) > len(longest_palindrome):
      longest_palindrome = palindrome

    # Check for palindromes of even length centered at this character
    palindrome = find_palindrome(string, i, i+1)
    if len(palindrome) > len(longest_palindrome):
      longest_palindrome = palindrome

  return longest_palindrome

def find_palindrome(string, left, right):
  # Continue expanding the palindrome as long as the left and right indices are valid
  # and the characters at those indices are the same
  while left >= 0 and right < len(string) and string[left] == string[right]:
    left -= 1
    right += 1

  # Return the palindrome, excluding the characters that caused the loop to exit
  return string[left+1:right]


s = "banana"

print (find_longest_palindrome(s) )
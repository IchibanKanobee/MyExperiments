#Write a Python function called find_unique_characters that takes a string as input and returns a list of all the unique characters in the string, in the order that they appear.
from typing import List

def find_unique_characters(s: str) -> List[str]:
    unique_list = []
    seen = set()
    for letter in s:
        if letter not in seen:
            unique_list.append(letter)
            seen.add(letter)
    return unique_list

word = 'hello'
print (find_unique_characters(word))
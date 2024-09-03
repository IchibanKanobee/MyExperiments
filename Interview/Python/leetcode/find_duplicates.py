#Write a Python function called find_duplicate_numbers that takes a list of integers as input and returns a list of all the duplicate numbers in the list.
from typing import List

def find_duplicate_numbers(numbers: List[int]) -> List[int]:
    duplicate_list = []
    seen = set()
    for n in numbers:
        if n in seen:
            duplicate_list.append(n)
        seen.add(n)
    return duplicate_list


print (find_duplicate_numbers([1, 2, 3, 3, 4, 5, 5]))
#Write a Python function called calculate_total_cost that takes a list of tuples as input and returns the total cost of all the items in the list.

#Each tuple in the list represents an item, and contains the item's price and quantity. The function should return the total cost of all the items, which is calculated by multiplying the price and quantity of each item.rom typing import List

from typing import List, Tuple

def calculate_total_cost(items: List[Tuple[int, int]]) -> int:
    total_cost = 0
    for item in items:
        total_cost = total_cost + item[0] * item[1]
    return total_cost


print (calculate_total_cost([(10, 2), (5, 3), (20, 1)]))
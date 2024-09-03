from collections import Counter

a = [1,1,1,2,3]
counts = Counter(a)

majority = None
m = max(counts, key=counts.get)
if counts[m] > len(a) / 2:
    majority = m
print(majority)


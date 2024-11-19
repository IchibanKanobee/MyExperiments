#Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

#Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.

def get_next_one_pos(bin_n, start_pos):
    count = len(bin_n)
    for i in range (start_pos, count):
        if (bin_n[i] == '1'):
            return i
    return None

def get_binary_gap(n):
    longest_dist = 0
    bin_n = bin(n)[2:]
    first_one = get_next_one_pos(bin_n, 0)
    if first_one is None:
        return longest_dist
    while True:
        next_one = get_next_one_pos(bin_n, first_one + 1)
        if next_one is None:
            return longest_dist
        dist = next_one - first_one
        if dist > longest_dist:
            longest_dist = dist
        first_one = next_one

    return (longest_dist)


def binaryGap(N):
    pre = dist = 0
    for i, c in enumerate(bin(N)[2:]):
        if c == "1":
            dist = max(dist, i - pre)
            pre = i
    return dist

#print(get_binary_gap(10))
print(binaryGap(10))

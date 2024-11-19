#The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

#Given two integers x and y, return the Hamming distance between them.

def get_hamming_distance(x:int, y:int)-> int:
    # dist = 0
    # xor_result = x ^ y
    # while xor_result != 0:
    #     if xor_result & 1:
    #         dist += 1
    #     xor_result >>= 1
    # return dist
    return bin(x ^ y).count('1')

print(get_hamming_distance(3, 5))

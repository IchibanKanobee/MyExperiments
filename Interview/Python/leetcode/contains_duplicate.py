nums = [1,2,3,1]

def is_duplicate(nums):
    s = set()
    for i in range(len(nums)):
        if nums[i] in s:
            return True
        s.add(nums[i])
    return False

print (is_duplicate(nums))



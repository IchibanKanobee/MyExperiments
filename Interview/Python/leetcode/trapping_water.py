#https://leetcode.com/problems/trapping-rain-water/
#Solution: https://www.youtube.com/watch?v=ZI2z5pq0TqA&t=186s&ab_channel=NeetCode

#My non optimal solution
def get_trapped_water(height):
#For each position i, the trapped water is amount = min(max(height[:h], max(height[h+1:])) - h[i] if > 0, else 0
    trapped = 0
    for i in range(1, len(height) - 1):
        left = height[:i]
        right = height[i+1:]
        amount = min(max(left), max(right)) - height[i]
        amount = amount if amount > 0 else 0
        trapped += amount
    return trapped

height = [0,1,0,2,1,0,1,3,2,1,2,1]

print(get_trapped_water(height))

---------------------------------------------------------------------
#Optimal solution with O(n) space complexity
max_left = [0] * len(height)
max_left[0] = 0
for i in range(1, len(height)):
    max_left[i] = height[i - 1] if height[i - 1] > max_left[i - 1] else max_left[i - 1]

max_right = [0] * len(height)
max_right[len(height) - 1] = 0
for i in range(len(height) - 2, -1, -1):
    max_right[i] = height[i + 1] if height[i + 1] > max_right[i + 1] else max_right[i + 1]

min_max = [0] * len(height)
for i in range(0, len(height)):
    min_max[i] = min(max_left[i], max_right[i])

trapped_water_optimal_O_n = 0
for i in range(len(height)):
    amount_i = min_max[i] - height[i]
    trapped_water_optimal_O_n += amount_i if amount_i > 0 else 0

print (trapped_water_optimal_O_n)
-------------------------------------------------------

#Optimal solution with O(1) space complexity
left_pointer = 0
right_pointer = len(height) - 1
max_left  = height[left_pointer]
max_right = height[right_pointer]
for i in range(1, len(height)):





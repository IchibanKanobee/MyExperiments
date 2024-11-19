from collections import Counter
#Robot returns to the origin if count('L') == count('R'), and count('D') == count('U')

robot_moves = ['L', 'R', 'U', 'D', 'R', 'R', 'U', 'D']
counts = Counter(robot_moves)
print (counts)
if counts['U'] == counts['D'] and counts['L'] == counts['R']:
    print('Robot returns to origin')
else:
    print("Robot doesn't return to origin")

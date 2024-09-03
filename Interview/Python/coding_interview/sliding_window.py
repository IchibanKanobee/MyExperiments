#https://www.educative.io/courses/grokking-coding-interview-patterns-python/RMkpmAllP9L

window_size = 3
array = [-4, 2, -5, 3, 6]

count = len(array)
i = 0
while(i + window_size <= count):
    print(max(array[i:i+window_size]))
    i += 1


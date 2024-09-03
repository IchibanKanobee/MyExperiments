#https://www.youtube.com/watch?v=HAgLH58IgJQ&ab_channel=NeetCode
number = 123456
reverse = 0
while(number> 0):
    remainder = number % 10
    number = number // 10
    if (number > 0):
        remainder *= 10
        reverse *= 10
    reverse = (reverse + remainder)

print(reverse)
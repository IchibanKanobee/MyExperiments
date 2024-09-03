#https://quescol.com/interview-preparation/armstrong-program-in-python
#Armstrong number is a number which is equal to the sum of cube of its digits.

def get_digits(number):
    digits = []
    while(number > 0):
        digit = number % 10
        digits.insert(0, digit)
        number = number // 10
    return digits

def get_sum_of_cubes(numbers):
    sum = 0
    count = len(numbers)
    for i in range(count):
        sum = sum + numbers[i]**3
    return sum

number = 153
digits = get_digits(number)
sum_of_cubes = get_sum_of_cubes(digits)

result = ("{} is an Armstrong number").format(number) if (sum_of_cubes == number) else ("{} is not an Armstrong number").format(number)
print(result)

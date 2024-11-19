
def plus_one(number):
    result = [0] * len(number)
    charge = 0
    for i in range(len(number) - 1, -1, -1):
        if i == len(number) - 1:
            result[i] = number[i] + 1 + charge
        else:
            result[i] = number[i] + charge

        if result[i] > 9:
            result[i] = result[i] % 10
            charge = 1
        else:
            charge = 0

        if i == 0 and charge == 1:
            result.insert(0,1)

    return result

def list_to_int(number_list):
    number = 0
    j = 0
    for i in range(len(number_list) - 1, -1, -1):
        number += pow(10, j) * number_list[i]
        j = j+ 1
    return number


def list_to_int2(number_list):
    number = 0
    for i in range(len(number_list)):
        number += pow(10, i) * number_list[len(number_list) - i -1]
    return number

def plus_one1(number_list):
    number = list_to_int2(number_list)
    return [int(s) for s in str(number + 1)]

number = [3,8,9,3,4,5,6,7,8,9,0,1,4,5,6,7,1]
print (plus_one(number))

#print (list_to_int2(number))


# num = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# print (num + 1)


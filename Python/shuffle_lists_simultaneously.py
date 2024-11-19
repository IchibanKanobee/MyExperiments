from random import shuffle


def shuffle_lists(*ls):
  l =list(zip(*ls))

  shuffle(l)
  return zip(*l)


a = [1,2,3,4,5]
b = ['a', 'b', 'c', 'd', 'e']
c = [11,22,33,44,55]

a1, b1, c1, = shuffle_lists(a, b, c)
print (a1)
print (b1)
print (c1)

def form_tuple(a):
    if ((a % 2) == 0):
        mode = "even"
    else:
        mode = "odd"
    return (a, mode)



class Dataset:
    def __init__(self):
        self.pointer = 0

    def get_next(self, count):
        res = []
        for i in range (self.pointer, self.pointer + count):
            tup = form_tuple(i)
            res.append(tup)
        self.pointer = self.pointer + count
        return res


data = Dataset()
a = data.get_next(10)
print a

b = data.get_next(5)
print b    

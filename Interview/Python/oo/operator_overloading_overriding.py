#Method overlaoding
#Methods with the same name but different parameters. In Python it is impossible, but we can pass default Nones to accomplish the same thing
#https://www.youtube.com/watch?v=CcTzTuIsoFk&ab_channel=Telusko
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        if a!= None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s=a
        return s

s = Student(100,200)
s1 = s.sum(1,2,3)
print(s1)
s2 = s.sum(2,3)
print(s2)
s3 = s.sum(2)
print(s3)

#Method overriding
class A:
    def show(self):
        print ("in A show")

class B(A):
    def show(self):
        print ("in B show")

a = A()
a.show()

b = B()
b.show()


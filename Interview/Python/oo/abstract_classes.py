#https://www.youtube.com/watch?v=n97Wm5P35KU&ab_channel=TechProgrammer
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

#s = Shape()

c = Circle()
c.draw()

sq = Square()
sq.draw()
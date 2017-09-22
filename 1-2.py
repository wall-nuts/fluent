#encoding:utf-8
from math import hypot
import os
class Vector:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r,%r)'%(self.x,self.y)

    def __abs__(self):
        return hypot(self.x,self.y)

    def __bool__(self):
        # return bool(abs(self))
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.y
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar,self.y * scalar)

#占位符_
_, filename = os.path.split('/home/lucano/.ssh/idrsa.pub')

#拆包
metro_areas = [('Tokyo','JP',36.933,(35.689722,139.691667)),]
for name, cc, pop,(latitude,longitude) in metro_areas:
    print('{:15} | {:9.4f} | {:9.4f}'.format(name,latitude,longitude))



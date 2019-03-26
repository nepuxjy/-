class Rectangle():
    def __init__(self,w,l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len
    def change_size(self,w,l):
        self.width = w
        self.len = l

rectangle = Rectangle(10,80)
print(rectangle.area())
rectangle.change_size(40,40)
print(rectangle.area())
class Data:
    def __init__(self):
        self.nums = [1,2,3,4,5]
    def change_data(self,index,n):
        self.nums[index] = n
data_one = Data()
data_one.nums[0]= 100
print(data_one.nums)
data_two = Data()
data_two.change_data(0,100)
print(data_two.nums)
class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner
class Person():
    def __init__(self,name):
        self.name = name
mick = Person("Mick Jagger")
stan = Dog("Stanley","Bulldog",mick)
print(stan.owner.name)
class Person:
    def __init__(self):
        self.name = 'Bob'
bob = Person()
same_bob = bob
print(bob is same_bob)
another_bob = Person()
ad = another_bob
print( bob is another_bob)
print(ad is another_bob)
print(ad is bob)

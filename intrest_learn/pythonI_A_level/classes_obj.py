import matplotlib.pyplot as plt
import numpy as np

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"hello mr/ms::{self.name} I assume you are aged {self.age}")

class Student(Person):
    def __init__(self,name, age, major):
        super().__init__(name, age)
        self.major = major

    def study(self):
        print(f" you are currently studying:: {self.major}")

person1 = Student("vivek", 34, "Artificial intelligence")
person2 = Person("vinu", 31)


# person1.greet()
# person1.study()
# person2.greet()


class Math:
    def add(self, x, y, z=None):
        if z:
            return x + y + z
        else:
            return x + y
        
# with open("file.txt", "w") as f:
#     f.write("learing to handle filesystem")

# with open("file.txt", "r") as f:
#     d = f.read()
    # print(d)

m1 = Math()
# print(m1.add(5,6,4))



x = np.linspace(0,10,1000)
y = np.sin(x)
# print(y)
plt.plot(x, y)
plt.show()

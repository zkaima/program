# 体脂换算

class Person:
    def __init__(self,name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height

    @property
    def bmi(self):
        return self.weight / (self.height * self.height)


p = Person("小明",50,1.5)
print(p.bmi)

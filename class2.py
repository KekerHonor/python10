class person:
    def __init__(self, name: str, age:int):
        self.name = name
        self.age = age
    def hi(self):
        print("Hi!","I am", self.name)
numbers = [1, 3, 2] # class list
names = ["a","z","c"] # class list
p = person("bold", 22)
p2 = person("baatar", 26)
print(p.name)
p.hi()
print(p2.name)
p2.hi()
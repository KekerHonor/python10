class person:
    fname = "bold"
    lname = "tumur"
    def hi(self):
        print("Hi, I'm ", self.fname)
p1=person()
p2=person()
print(p1.fname)
p1.hi()
print(p2.fname)
p2.hi()
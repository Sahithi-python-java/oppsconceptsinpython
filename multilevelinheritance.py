class GrandParent():
    def outputgp(self):
        print("I am GrandFather")
class Parent(GrandParent):
    def outputp(self):
        print("I am Parent")
class Child(Parent):
    def outputc(self):
        print("I am Child")

c=Child()
c.outputgp()
c.outputp()
c.outputc()
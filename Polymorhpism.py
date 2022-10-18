#parent class Class
class Class:
    attribute 1 = ''
    attribute 2 = ''
    attribute 3 = ''
    def Method1(self):
        print("Method 1")
    def Method2(self):
        print("Method 2")
#Child class 1
#note the polymorphism. Attribute 3 and Method1() are overridden here
class Child1(Class):
    attribute 3 = ''
    attribute 4 = ''
    attribute 5 = ''
    def Method1(self):
        print("Variation on Method1")

#Child class 2
#note the polymorphism. Attribute 2 and Method2() are overridden here    
class Child2(Class):
    attribute 2 = ''
    attribute 6 = ''
    attribute 7 = ''
    def Method2(self):
        print("Variation on Method 2")

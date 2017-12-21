class Person(object):
    def __init__(self, age,name):
        self.age = age
        self.name = name

class Woman(Person):
    def sing(self):
        print "Lalalala lala"

class Man(Person):
    def dance(self):
        print "Trapp Trapp Trapp"

if __name__ == '__main__':
    p = Person (19, "Karen")
    print p.age
    print p.name

    olivia = Woman(20, "Olivia")
    olivia.sing()

    oli = Man(20, "Oli")
    #oli.sing() # Man can't sing, this will cause an error
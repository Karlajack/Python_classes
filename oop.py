
class Person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age        
        self.height=height

    def eat(self):
            return 'I love food!'
            
    def drive(self):
            return 'I drive Subaru!'



myPerson=Person("jack doe",29,160)

print(myPerson.name)
print(myPerson.age)
print(myPerson.height)
print(myPerson.eat())
print(myPerson.drive())
print(Person)
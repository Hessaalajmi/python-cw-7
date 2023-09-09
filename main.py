class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def is_adult(self):
        if self.age >= 18:
            print('You have too much responsibilities')
        else:
            print('Lucky you')
    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old '    
    

first_person = person('hessa', 14)
print(first_person.name)
print(first_person.age)
print(first_person.is_adult())
print(first_person)

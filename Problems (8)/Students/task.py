class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = self.name[0:1] + self.last_name + str(self.birth_year)


use_info = []
for info in range(3):
    use_info.append(input())

name, last_name, birth_year = [x for x in use_info]
print(Student(name, last_name, birth_year).id)

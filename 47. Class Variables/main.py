class Student:
    school ="Indian public school"
    NoOfStudents = 0
    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll
        Student.NoOfStudents+=1

    def __str__(self):
        return f"{self.name} {self.school} {self.age} {self.roll} {self.NoOfStudents}"

s1 = Student("AK", 18, 10)
print(s1)
s2 = Student("AK2", 20, 11)

print(s2)

Student.school = "Indian school"
print(s1)
print(s2)
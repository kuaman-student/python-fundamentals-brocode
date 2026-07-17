# Class methods Allow operations related to the class itself
# Take (cls) as the first parameter, which represents the class itself.

class Student:
    count = 0
    total_cgpa = 0
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
        Student.count+=1
        Student.total_cgpa += cgpa

    def get_info(self):
        return f"{self.name} {self.cgpa}"

    @classmethod
    def get_count(cls):
        return f"Total students = {cls.count}"
    @classmethod
    def get_avg_cgpa(cls):
        return f"Avg CGPA = {cls.total_cgpa/cls.count:.2f}"


s1 = Student("A", 9.2)
s2 = Student("B", 9)
s3 = Student("C", 4.2)

print(Student.get_count())
print(Student.get_avg_cgpa())
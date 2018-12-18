class Student:
    def __init__(self, id: int, name: str, gpa: float):
        self.id = id
        self.name = name
        self.gpa = gpa

class StudentClass:
    def __init__(self):
        self.__student_list = []

    def add_student(self, student: Student):
            self.__student_list.append(student)
    def remove_student(self, student_id:int):
        for current_student in self.__student_list:
            if current_student.id == student_id:
                self.__student_list.remove(current_student)
    def list_student(self):
        for student in self.__student_list:
            print(("Student ID: " + str(student.id) + "Student name " + student.name))

    def get__count_student(self):
        return len(self.__student_list)

    def get__average_gpa(self):

        gpa_total = 0

        for student in self.__student_list:
            gpa_total = gpa_total + student.gpa

        average_gpa = gpa_total/len(self.__student_list)

        return average_gpa
        return gpa_total / self.get_count_student()

math_101 = StudentClass()
physics_101 = StudentClass()

s1 = Student(1, "Mary", 2.8)
s2 = Student(2, "Bob", 2.0)
s3 = Student(3, "Brendon", 3.2)

math_101.add_student(s1)
math_101.add_student(s2)
math_101.add_student(s3)
math_101.remove_student(s2)


print("The average of remaining student is " + str(math_101.get__average_gpa()))
print("The average of remaining student is " + str(math_101.get__count_student()))








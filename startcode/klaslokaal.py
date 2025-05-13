from student import Student
class Klaslokaal:
    def __init__(self):
        self.studenten = []

    def voeg_student_toe(self, student):
        self.studenten.append(student)

    def toon_studenten(self):
        print("Studenten in de klas:")
        for student in self.studenten:
            student.stel_voor()

student1 = Student("Lotte", 20)
student2 = Student("Jasper", 21)
klaslokaal = Klaslokaal()
klaslokaal.voeg_student_toe(student1)
klaslokaal.voeg_student_toe(student2)
klaslokaal.toon_studenten()
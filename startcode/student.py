class Student:
    def __init__(self,naam,leeftijd):
        self.naam =  naam
        self.leeftijd = leeftijd

    def stel_voor(self):
        print(f"Mijn naam is {self.naam} en ik ben {self.leeftijd} jaar oud.")


student1 = Student("Floor Mat", 18)
student2 = Student("Ron De Bril", 17)

student1.stel_voor()
student2.stel_voor()

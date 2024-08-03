class Students:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def insertG(self, numG):
        self.numG = numG
        self.grades = []
        for i in range(0, numG, 1):
            prompt = float(input('Please Enter Grade: '))
            self.grades.append(prompt)
        return self.grades

student = Students('Ramiro', 'Santos')
student1 = Students('Jaime', 'Carlos')
print(student.first, student.last)
print(student1.first, student1.last)

testGrd = student.insertG(4)
print(testGrd)
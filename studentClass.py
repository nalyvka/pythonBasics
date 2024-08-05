class Students:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def insert(self,ng):
        self.ng = ng
        self.grades = []
        for i in range(0, ng, 1):
            prompt = float(input('Please Enter Grade: '))
            self.grades.append(prompt)
        return self.grades
    def printGrades(self):
        print(self.first, self.last, "'s", 'Grades Are: ')
        print('')
        for i in range(0, self.ng, 1):
            print(self.grades[i])
        print('')
    
    def lowHigh(self):
        lowVal = 100
        highVal = 0
        for i in self.grades:
            if i < lowVal:
                lowVal = i
            if i > highVal:
                highVal = i

#objects
student = Students('John', 'Dee')
student1 = Students('Emil', 'Cioran')

#specify the # of grades for each student
numG = student.insert(2)
numG1 = student1.insert(3)

test = student.printGrades()
test1 = student1.printGrades()
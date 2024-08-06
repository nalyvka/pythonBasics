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
        return lowVal, highVal
    def avg(self):
        bucket = 0
        for i in range(0, self.ng, 1):
            bucket = bucket + self.grades[i]
        average = bucket / self.ng
        return average
    def bubbleSort(self):
        swapper = 0
        self.bub = self.grades
        for i in range(0, self.ng-1, 1):
            for i in range(0, self.ng-1, 1):
                if self.bub[i] < self.bub[i+1]:
                    swapper = self.bub[i]
                    self.bub[i] = self.bub[i+1]
                    self.bub[i+1] = swapper
        return self.bub

#objects
student = Students('John', 'Dee')
student1 = Students('Emil', 'Cioran')
numGrade = student.insert(2)
numGrade1 = student1.insert(3)
student.printGrades()
student1.printGrades()
low, high = student.lowHigh()
print(student.first, student.last, "'s", 'Highest Grade: ', high)
print(student.first, student.last, "'s", 'Lowest Grade: ', low)
average = student.avg()
print(student.first, student.last, 'Has An Average Of ', average)
sortedGrades = student.bubbleSort()
print(student.first, student.last, "'s", 'Sorted Grades Are ', sortedGrades)
print('')
low1, high1 = student1.lowHigh()
print(student1.first, student1.last, "'s", 'Highest Grade: ', high)
print(student1.first, student1.last, "'s", 'Lowest Grade: ', low)
average1 = student1.avg()
print(student1.first, student1.last, 'Has An Average Of ', average1)
sortedGrades1 = student1.bubbleSort()
print(student1.first, student1.last, "'s", 'Sorted Grades Are ', sortedGrades1)
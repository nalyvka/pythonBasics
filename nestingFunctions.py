def inputGrades(x):
    grades = []
    for i in range(0, x, 1):
        prompt = input('Please Enter Your Grades: ')
        grades.append(prompt)
        print(grades[i])
        return grades
def avGrades(x):
    
numGrades = 5
iG = inputGrades(numGrades)
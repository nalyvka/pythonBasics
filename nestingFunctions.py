def inputGrades(x):
    grades = []
    for i in range(0, x, 1):
        prompt = float(input('Please Enter Your Grades: '))
        grades.append(prompt)
    return grades
def printGrades(x, y):
    for i in range(0, x, 1):
        print(y[i])
    return y
def avGrades(x,y):
    bucket = 0
    for i in range(0, x, 1):
        bucket = bucket + y[i]
    return bucket
numGrades = 2
iG = inputGrades(numGrades)
pG = printGrades(numGrades, iG)

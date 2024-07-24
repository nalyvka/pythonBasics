bucket = 0
def inputGrades(x):
    grades = []
    for i in range(0, x, 1):
        prompt = float(input('Please Enter Your Grades: '))
        grades.append(prompt)
    return grades
def avGrades(x, y):
    for i in range(0, x, 1):
        bucket = bucket + grades[i]
    return bucket

numGrades = 5
iG = inputGrades(numGrades)
print('Your Grades Are: ', iG)
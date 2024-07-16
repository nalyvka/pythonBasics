numGrades = int(input('Please Enter The # of Grades: '))
grades = []
bucket = 0
for i in range(0, numGrades, 1):
    grade = float(input('Please Enter Your Grade: '))
    grades.append(grade)
for i in range(0, numGrades, 1):
    bucket = bucket + grades[i]
for i in range(0, numGrades, 1):
    print(grades[i])
avg = bucket / numGrades
print('Your Average Is: ', avg)
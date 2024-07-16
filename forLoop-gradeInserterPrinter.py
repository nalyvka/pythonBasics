numGrades = int(input('Please Enter The # of Grades: '))
grades = []
for i in range(0, numGrades, 1):
    grade = input('Please Enter Your Grade: ')
    grades.append(grade)
for i in range(0, numGrades, 1):
    print(grades[i])
numGrades = int(input('Please Enter Your # Grades: '))
j = 0
grades = []
while (j<numGrades):
    entGrades= float(input('Please Enter Your Grades: '))
    grades.append(entGrades)
    j=j+1
j = 0
while (j<numGrades):
    print(grades[j])
    j=j+1
print('Thank You For Your Time')
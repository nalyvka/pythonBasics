grades = []
bucket = 0
lowVal = 100
highVal = 0
swapper = 0
numGrades = int(input('Please Enter The # of Grades: '))
avg = bucket / numGrades

#user generated array: prompts user to insert grades and appends them to an array
for i in range(0, numGrades, 1):
    grade = float(input('Please Enter Your Grade: '))
    grades.append(grade)

#finds the average of the grades
for i in range(0, numGrades, 1):
    bucket = bucket + grades[i]


#finds the smallest and highest grades in the array
for i in grades:
    if i < lowVal:
        lowVal = i
    if i > highVal:
        highVal = i

#bubble sort algorithm
for i in range(0, numGrades-1, 1):
    for i in range(0, numGrades-1, 1):
        if grades[i] < grades[i+1]:
            swapper = grades[i]
            grades[i] = grades[i+1]
            grades[i+1] = swapper

#prints the user-inputted grades one by one
for i in range(0, numGrades, 1):
    print(grades[i])
    
print('Your High value is: ', highVal)
print('Your Low value is: ', lowVal)
print('Your Average Is: ', avg)

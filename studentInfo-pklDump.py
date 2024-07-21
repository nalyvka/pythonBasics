import pickle
numStudents = int(input('Please enter the # of students: '))
names = []
idValues = []
age = []
gpa = []


for i in range(0,numStudents, 1):

    namePrompt = input("Please enter the student's name: ")
    names.append(namePrompt)

    idPrompt = int(input('Please enter ' + namePrompt + 's ID#: '))
    idValues.append(idPrompt)

    agePrompt = int(input('Please enter ' + namePrompt + 's age: '))
    age.append(agePrompt)

    gpaPrompt = float(input('Please enter ' + namePrompt + 's GPA: '))
    gpa.append(gpaPrompt)

with open('studentFile.pkl', 'wb') as dat:
    pickle.dump(numStudents, dat)
    pickle.dump(names, dat)
    pickle.dump(age, dat)
    pickle.dump(gpa, dat)
import pickle
with open('studentFile.pkl', 'rb') as read:
    numStudents = pickle.load(read)
    names = pickle.load(read)
    idValues = pickle.load(read)
    age = pickle.load(read)
    gpa = pickle.load(read)

#infinite loop
while (0==0):
    namePrompt = input('Which student do you want to check up ')
    for i in range(0, numStudents, 1):
        if (names[i]==namePrompt):
            print(namePrompt, "'s ID is ", idValues[i], '.')
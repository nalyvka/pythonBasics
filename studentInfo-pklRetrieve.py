import pickle
with open('studentFile.pkl', 'rb') as read:
    numStudents = pickle.load(read)
    names = pickle.load(read)
    age = pickle.load(read)
    gpa = pickle.load(read)
x = input('Which student are you interested in? ')
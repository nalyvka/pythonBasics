import pickle
x = input("Are You Ready To See Some Data? ")
if (x=='yes' or x=='Yes' or x == 'YEs' or x=='YeS' or x=='YES'):
    with open('data.pkl', 'rb') as reykjavik:
        i = pickle.load(reykjavik)
        j = pickle.load(reykjavik)
        k = pickle.load(reykjavik)
        print('Your Foods Are: ', i)
        print('Your Drinks Are: ', j)
        print('Your Favorite Number Is: ', k)

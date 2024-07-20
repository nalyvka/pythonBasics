import pickle
foods = ['skyr', 'pirozhki', 'blini', 'golubtsy']
drinks = ['brennivin', 'reykaVodka', 'egils-sterkur', 'opal']
favNum = 3.14159265359
with open('data.pkl', 'wb') as kazan:
    pickle.dump(foods, kazan)
    pickle.dump(drinks, kazan)
    pickle.dump(favNum, kazan)
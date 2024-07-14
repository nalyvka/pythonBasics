myNum = int(input('Please Enter Your Number: '))
if (myNum % 2 == 0 and myNum > 0):
    print('Your Number Is Even & Postive')
if (myNum % 2 != 0 and myNum > 0):
    print('Your Number Is Odd & Positive')
if (myNum % 2 == 0 and myNum < 0):
    print('Your Number Is Even & Negative')
if (myNum % 2 != 0 and myNum < 0):
    print('Your Number Is Odd & Negative')
if (myNum == 0):
    print('Your Number Is Zero')

def sumNum(num, num1):
    nums = num + num1
    return nums
prompt = float(input('Please Enter Your First Number: '))
prompt1 = float(input('Please Enter Your Second Number: '))
catch = sumNum(prompt, prompt1)
print('The Sum of', prompt, '+', prompt1, 'Is ', catch)
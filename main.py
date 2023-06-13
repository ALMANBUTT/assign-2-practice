from add import add
from subtract import subtarct
from multiply import multiply

#taking input from user
num1=int(input('enter 1st number: '))
num2=int(input('enter 2nd number: '))
result=add(num1,num2)
print('The Sum of Two Number is: ',result)


#taking input from user
num1=int(input('enter 1st number: '))
num2=int(input('enter 2nd number: '))
result=subtarct(num1,num2)
print('The Subtract of Two Number is: ',result)


#taking input from user
num1=int(input('enter 1st number: '))
num2=int(input('enter 2nd number: '))
result=multiply(num1,num2)
print('The Multiply of Two Number is: ',result)
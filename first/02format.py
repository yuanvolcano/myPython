age = 20
name = 'Swaroop'
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name, age))
print('{0:.3f}'.format(1.0/3))
print('{:.4f}'.format(4.1))
# < ^ > 分别代表左对齐、居中、右对齐
print('{:^14}'.format('陈某某')) 
print('{:<14}'.format('陈某某')) 
print('{:\'>14}'.format('陈某某'))
print('{0:_^11}'.format('hello'))
print('{0:_<11}'.format('hello'))
# b o d x 分别代表二级制、八进制、十进制、16进制
print('{:b}'.format(250))  
print('{:o}'.format(250))
print('{:d}'.format(250))
print('{:x}'.format(250))
print('{:,}'.format(100000000))
print('{:,}'.format(10))
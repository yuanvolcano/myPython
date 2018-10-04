# python 语法

## 数字

数字主要分为两种类型--整数和浮点数

2 是一个整数，3.23或52.3E-4是一个浮点数,在这里，E表示10的幂。

## 字符串

### 单引号

'quote me'

### 双引号

"What's your name?"

单引号和双引号工作机制完全相同

### 三引号


你可以通过使用三个引号---'''或"""来指定多行字符串，你可以在三引号之间自由地使用单引号与双引号。
```
'''这是一段多行字符串。这是它的第一行。
This is the second line.
"What's your name?," I asked.
He said
'''
```

### 字符串是不可变的

这意味着一旦你创造了一串字符串，你就不能再改变它。尽管这看起来像是一件坏事，但实际上并非如此。


## 运算符

*  +（加）

    * 两个对象相加。
    * 3+5 则输出9。'a' + 'b' 则输出'ab'

*  -（减）
    
    * 从一个数中减去另一个数，如果第一个操作数不存在，则假定为零。
    * -5.2 将输出一个负数， 50 - 24 输出 26 。
  
*  *（乘）
    
    * 给出两个数的乘积，或返回字符串重复指定次数后的结果。
    * 2 * 3 输出 6 。 'la' * 3 输出 'lalala' 。  

*  **（乘方）
    
    * 返回 x 的 y 次方。
    * 3 ** 4 输出 81 （即 3 * 3 * 3 * 3 ）。

*  /（除）
    
    * x 除以 y。
    * 13 / 3 输出 4.333333333333333 。 

*  //（整除）

    * x 除以 y 并对结果向下取整至最接近的整数。
    * 13 // 3 输出 4 。
    * -13 // 3 输出 -5 。

*  %（取模）
    
    * 返回除法运算后的余数。
    * 13 % 3 输出 1 。 -25.5 % 2.25 输出 1.5 。
  
*  <<（左移）
    
    * 将数字的位向左移动指定的位数。（每个数字在内存中以二进制数表示，即 0 和1）
    * 2 << 2 输出 8 。 2 用二进制数表示为 10 。
    * 向左移 2 位会得到 1000 这一结果，表示十进制中的 8 。

*  \>\>（右移）
    
    * 将数字的位向右移动指定的位数。
    * 11 >> 1 输出 5 。
    * 11 在二进制中表示为 1011 ，右移一位后输出 101 这一结果，表示十进制中的5 。

*  &（按位与）
    
    * 对数字进行按位与操作。。
    * 5 & 3 输出 1。 

*  |（按位或）

    * 对数字进行按位或操作。
    * 5 | 3 输出 7 。
    
*  ^（按位异或）

    * 对数字进行按位异或操作。
    * 5^3输出7

*  -（按位取反）
    
    * x 的按位取反结果为 -(x+1)。
    * -5 输出 -6 。
  
*  <（小于）
    
    * 返回 x 是否小于 y。所有的比较运算符返回的结果均为 True 或 False 。请注意这些名称之中的大写字母。
    * 5 < 3 输出 False ， 3 < 6 输出 True 。 
    * 比较可以任意组成组成链接： 3 < 5 < 7 返回 True 。 

*  \>（大于）
    
    * 返回 x 是否大于 y。
    * 5 > 3 返回 True 。如果两个操作数均为数字，它们首先将会被转换至一种共同的类型。否则，它将总是返回 False 。

*  \>=（大于等于）
    
    * 返回 x 是否大于或等于 y。
    * x = 4; y = 3; x>=3 返回 True 。

*  <=（小于等于）

    * 返回 x 是否小于或等于 y。
    * x = 3; y = 6; x<=y 返回 True 。

*  ==（等于）
    
    * 比较两个对象是否相等。
    * x = 2; y = 2; x == y 返回 True 。
    * -5 输出 -6 。
    * x = 'str'; y = 'stR'; x == y 返回 False 。
    * x = 'str'; y = 'str'; x == y 返回 True 。
  
*  !=（不等于）
    
    * 比较两个对象是否不相等。
    * x = 2; y = 3; x != y 返回 True 。 

*  not（布尔“非”）
    
    * 如果 x 是 Ture ，则返回 False 。如果 x 是 False ，则返回 True 。
    * x = Ture; not x 返回 False 。

*  and（布尔“与”）
    
    * 如果 x 是 False ，则 x and y 返回 False ，否则返回 y 的计算值。
    * 当 x 是 False 时， x = False; y = True; x and y 将返回 False 。在这一情境中，Python 将不会计算 y，因为它经了解 and 表达式的左侧是 False ，这意味着整个表达式都将是 False 而不会是别的值。这种情况被称作短路计算（Short-circuitEvaluation）。 

*  or（布尔“或”）
    
    * 如果 x 是 True ，则返回 True ，否则它将返回 y 的计算值。
    * x = Ture; y = False; x or y 将返回 Ture 。在这里短路计算同样适用。

## 控制流

### if语句

if 语句用以检查条件：如果 条件为真（True），我们将运行一块语句（称作 if-block 或 if块），否则 我们将运行另一块语句（称作 else-block 或 else 块）。其中 else 从句是可选的。
```
number = 23
guess = int(input('Enter an integer : '))
if guess == number:
  # 新块从这里开始
  print('Congratulations, you guessed it.')
  print('(but you do not win any prizes!)')
# 新块在这里结束
elif guess < number:
  # 另一代码块
  print('No, it is a little higher than that')
  # 你可以在此做任何你希望在该代码块内进行的事情
else:
  print('No, it is a little lower than that')
  # 你必须通过猜测一个大于（>）设置数的数字来到达这里。
print('Done')
```
输出：
```
$ python if.py
Enter an integer : 50
No, it is a little lower than that
Done
$ python if.py
Enter an integer : 22
No, it is a little higher than that
Done
$ python if.py
Enter an integer : 23
Congratulations, you guessed it.
(but you do not win any prizes!)
Done
```

### while 语句
while 语句能够让你在条件为真的前提下重复执行某块语句。 while 语句是 循环（Looping） 语句的一种。 while 语句同样可以拥有 else 子句作为可选选项。
```
number = 23
running = True
while running:
  guess = int(input('Enter an integer : '))
  if guess == number:
    print('Congratulations, you guessed it.')
    # 这将导致 while 循环中止
    running = False
  elif guess < number:
    print('No, it is a little higher than that.')
  else:
    print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
# 在这里你可以做你想做的任何事
print('Done')
```
输出
```
$ python while.py
Enter an integer : 50
No, it is a little lower than that.
Enter an integer : 22
No, it is a little higher than that.
Enter an integer : 23
Congratulations, you guessed it.
The while loop is over.
Done
```

### for语句

for...in 语句是另一种循环语句，其特点是会在一系列对象上进行迭代（Iterates），意即
它会遍历序列中的每一个项目。
```
for i in range(1, 5):
  print(i)
else:
  print('The for loop is over')
```
输出
```
$ python for.py
1
2
3
4
The for loop is over
```

### break语句

break 语句用以中断（Break）循环语句，也就是中止循环语句的执行，即使循环条件没有变更为False，或队列中的项目尚未完全迭代依旧如此。有一点需要尤其注意，如果你的中断了一个 for 或 while 循环，任何相应循环中的else 块都将不会被执行。
```
while True:
  s = input('Enter something:')
  if s == 'quit':
    break
  print('Length of the string is', len(s))
print('Done')
```
输出：
```
python break.py
Enter something : Programming is fun
Length of the string is 18
Enter something : quit
Done
```
### continue 语句

continue 语句用以告诉 Python 跳过当前循环块中的剩余语句，并继续该循环的下一次迭代。
```
while True:
  s = input('enter something:')
  if s == 'quit':
    break
  if len(s) < 3:
    print('Too small')
    continue
  print('input is of sufficient length')
```

输出：
```
$ python continue.py
Enter something : a
Too small
Enter something : 12
Too small
Enter something : abc
Input is of sufficient length
Enter something : quit
```

## 函数

函数（Functions）是指可重复使用的程序片段。它们允许你为某个代码块赋予名字，允许你通过这一特殊的名字在你的程序任何地方来运行代码块，并可重复任何次数。这就是所谓的调用（Calling）函数。

函数可以通过关键字 def 来定义。这一关键字后跟一个函数的标识符名称，再跟一对圆括号，其中可以包括一些变量的名称，再以冒号结尾，结束这一行。随后而来的语句块是函数的一部分。

```
def say_hello():
  print('hello world')

say_hello()
```
输出：
```
python function1.py
hello world
```

### 函数参数
函数可以获取参数，这个参数的值由你所提供，借此，函数便可以利用这些值来做一些事情。这些参数与变量类似，这些变量的值在我们调用函数时已被定义，且在函数运行时均已赋值完成。

函数中的参数通过将其放置在用以定义函数的一对圆括号中指定，并通过逗号予以分隔。当我们调用函数时，我们以同样的形式提供需要的值。要注意在此使用的术语——在定义函数时给定的名称称作“形参”（Parameters），在调用函数时你所提供给函数的值称作“实参”（Arguments）。

```
def print_max(a, b):
  if a > b:
    print(a, 'is maximum')
  elif a == b:
    print(a, 'is equal to', b)
  else:
    print(b, 'is maximum')

print_max(5, 6)
```
### 局部变量

当你在一个函数的定义中声明变量时，它们不会以任何方式与身处函数之外但具有相同名称的变量产生关系，也就是说，这些变量名只存在于函数这一局部（Local）。这被称为变量的作用域（Scope）。

```
x = 50

def func(x):
  print('x is', x)
  x = 2
  print('change local x to', x)

func(x)

print('x is still', x)
```

输出
```
python function_local.py
x is 50
Changed local x to 2
x is still 50
```

### global语句

如果你想给一个在程序顶层的变量赋值（也就是说它不存在于任何作用域中，无论是函数还是类），那么你必须告诉 Python 这一变量并非局部的，而是全局（Global）的。我们需要通过 global 语句来完成这件事。

```
x = 50

def func():
  global x
  print('x is', x)
  x = 2
  print('x is', x)

func()
```
输出
```
python function_global.py
x is 50
Changed global x to 2
```

### 默认参数值

对于一些函数来说，你可能为希望使一些参数可选并使用默认的值，以避免用户不想为他们提供值的情况。在函数定义时附加一个赋值运算符（ = ）来为参数指定默认参数值。

```
def say(message, times=1):
  print(message * times)
  
say('Hello')
say('World', 5)
```

### 关键字参数

如果你有一些具有许多参数的函数，而你又希望只对其中的一些进行指定，那么你可以通过命名它们来给这些参数赋值——这就是关键字参数（Keyword Arguments）——我们使用命名（关键字）而非位置（一直以来我们所使用的方式）来指定函数中的参数。

```
def func(a, b = 2, c = 3):
  print('a is', a, 'b is', b, 'c is', c)

func(3, 7)

func(23, b = 4, c = 5)
```

### 可变参数

有时你可能想定义的函数里面能够有任意数量的变量，也就是参数数量是可变的，这可以通过使用星号来实现。

```
def total(a = 5, *numbers, **phonebook):
  print('a', a)

  for single_item in numbers:
    print('single_item', single_item)

  for first_part, second_part in phonebook.items():
    print(first_part, second_part)
  
total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560)
```

### return语句

return 语句用于从函数中返回，也就是中断函数。我们也可以选择在中断函数时从函数中返回一个值。

```
def maximum (x, y):
  if x > y:
    return x
  elif x == y:
    return 'The numbers are equal'
  else:
    return y

print(maximum(5, 6))
```

如果 return 语句没有搭配任何一个值则代表着 返回 None 。 None 在 Python 中一个特殊的类型，代表着虚无。举个例子， 它用于指示一个变量没有值，如果有值则它的值便是 None（虚无） 。每一个函数都在其末尾隐含了一句 return None ，除非你写了你自己的 return 语句。

```
def some_function():
  pass

print(some_function())
```

Python 中的 pass 语句用于指示一个没有内容的语句块。

### DocStrings

函数的第一行逻辑行中的字符串是该函数的 文档字符串（DocString）。这里要注意文档字符串也适用于后面相关章节将提到的模块（Modules）与类（Class） 。

该文档字符串所约定的是一串多行字符串，其中第一行以某一大写字母开始，以句号结束。第二行为空行，后跟的第三行开始是任何详细的解释说明。

```
def print_max(x, y):
    '''Prints the maximum of two numbers. 

    The two values must be integers.'''

    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)
    if x > y:
      print(x, 'is maximum')
    else:
      print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
```
输出：
```
5 is maximum
Prints the maximum of two numbers.
The two values must be integers.
```


x = 50

def func():
  global x
  print('x is', x)
  x = 2
  print('x is', x)

func()

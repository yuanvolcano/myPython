while True:
  s = input('enter something:')
  if s == 'quit':
    break
  if len(s) < 3:
    print('Too small')
    continue
  print('input is of sufficient length')
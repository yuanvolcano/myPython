import sys
import time
f = None
try:
  f = open('poem.txt')
  # 我们通常读取文件的语句
  while True:
    line = f.readline()
    if len(line) == 0:
      break
    print(line, end=' ')
    sys.stdout.flush()
    # 让程序保持运行一段时间
    time.sleep(2)
except IOError:
  print('Could not find file poem.txt')
except KeyboardInterrupt:
  print('!! You cancelled the reading from the file.')

finally:
  if f:
    f.close()
  print('(cleaming up: Closed the file)')
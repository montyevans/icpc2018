'''
Tightly Packed
'''
import math

def __main__():
  n = long(raw_input())
  minDiff = float("inf")

  x = long(math.ceil(math.sqrt(n)))
  while True:
    y = (math.ceil(n / float(x)))
    if x > 2*y: break

    diff = x*long(y) - n
    if diff < minDiff and diff >= 0:
      minDiff = int(diff)
      if minDiff is 0: break

    x += 1

  print minDiff

__main__()

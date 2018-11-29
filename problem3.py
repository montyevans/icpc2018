import math

def mag(p):
  return math.sqrt(p[0]**2 + p[1]**2)

def dot(a, b):
  return a[0] * b[0] + a[1] * b[1]

def minMax(points):
  minVal = float("inf")
  for i in range(len(points)):
    p = points[i]
    qIndex = (i + 1) % len(points)
    q = points[qIndex]

    # Find unit normal vector to the line PQ
    qToP = [p[0] - q[0], p[1] - q[1]]
    normal = [-qToP[1], qToP[0]]
    unitNormal = [float(normal[0]) / mag(normal), float(normal[1]) / mag(normal)]

    # Dot it with vectors from p to all the other points. Call that generic, other point 'x'
    maxLen = 0.0
    for j in range(len(points)):
      if j is i or j is qIndex: continue
      x = points[j]
      pToX = [x[0] - p[0], x[1] - p[1]]
      perpLen = abs(dot(unitNormal, pToX))
      if perpLen > maxLen: maxLen = perpLen

    if maxLen < minVal: minVal = maxLen

  return minVal

def getPoints():
  N = int(raw_input())
  points = []
  for i in range(N):
    line = raw_input().split()
    points.append([float(x) for x in line])
  return points

def getPoints2():
  points = []
  lines = open("./inputs/problem3.txt").read().split("\n")
  N = int(lines[0])

  for i in range(N):
    line = lines[i + 1].split()
    if (not len(line)): continue
    points.append([float(x) for x in line])
  return points


def __main__():
  points = getPoints()

  print(minMax(points))

__main__()

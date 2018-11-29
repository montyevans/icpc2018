'''
Lost Is Close To Lose
'''

def getCores1():
  allCores = set()
  while True:
    line = raw_input()
    if(line == "***"):
      break
    words = line.split()
    for w in words:
      core = getCore(w)
      if(len(core) is not 0): allCores.add(core)
  return allCores

def getCore(word):
  core = ""
  for ch in word:
    if not ch.isalpha(): continue
    core += ch.lower()
  return core

def delAtPos(string, index):
  pre = string[:index]
  post = string[index + 1:]
  return pre + post

def transAtPos(string, index):
  return string[:index] + string[index + 1] + string[index] + string[index + 2:]

def isSimilar(core1, core2):
  if (len(core1) < len(core2)): #WLOG, core1 is longer | they are equal
    tmp = core1
    core1 = core2
    core2 = tmp

  if (len(core1) > len(core2) + 1): return False # No way to make up 2 char difference
  if (len(core1) is len(core2) + 1): # The only way to make a 1 char difference is with a deletion
    for i in range(len(core1)):
      if (delAtPos(core1, i) == core2): return True
    return False

  if (len(core1) is len(core2)): # Then check swaps & replacements
    # First check replacements
    numDiff = 0
    for i in range(len(core1)):
      if(core1[i] != core2[i]): numDiff += 1
    if numDiff is 1: return True

    # Now check transposes
    for i in range(len(core1) - 1):
      if (transAtPos(core1, i) == core2): return True
    return False


def getSimilars(coreSet):
  similars = {}
  for core in coreSet:
    for otherCore in coreSet:
      if core == otherCore: continue
      if isSimilar(core, otherCore):
        if core not in similars:
          similars[core] = []
        similars[core].append(otherCore)
  return similars


def printSimilars(similars):
  if len(similars) is 0:
    print "***"
  else:
    keys = sorted(similars.keys())
    for key in keys:
      line = key + ": " + " ".join(sorted(similars[key]))
      print line


def __main__():
  allCores = getCores1()
  similars = getSimilars(allCores)
  printSimilars(similars)

__main__()

import os

currentPath = os.path.dirname(os.path.realpath(__file__))
lineNumber = 0

for root, dirs, files in os.walk(currentPath, topdown=True):
   for name in files:
     if name.endswith('.cpp'):
      with open(root + "//" + name) as f:
        lineNumber = 0
        for line in f:
          lineNumber += 1
          if '//nocommit' in line:
            print("Found a nocommit in " + name + " at line " + str(lineNumber))
            f.close()
            break
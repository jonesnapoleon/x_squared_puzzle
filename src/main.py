from utils import fileToIntArray, setupOutputFile, printFail, matrixToArray
from rule import isReachable, siblingIndices


setupOutputFile()
array = fileToIntArray()

if not isReachable(array):
    printFail()
else:
    siblingIndices = siblingIndices(array)
    print(siblingIndices)





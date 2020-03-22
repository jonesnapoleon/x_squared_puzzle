from utils import fileToIntArray, setupOutputFile, desiredOutput
from utils import printFail, printArrayWithProgress, printSiblingCost, printSuccess
from rule import isReachable, getSiblingIndices, cost, decideNextArray, enque


setupOutputFile()
array = fileToIntArray()
desiredArray = desiredOutput(array)

if not isReachable(array):
    printFail()
else:
    nextArray = [num for num in array]
    path = 0
    nextData = {'sequence': nextArray, 'cost': 0, 'prevAction': '', 'path': path}
    progress = 0
    queue = []

    while nextArray != desiredArray:
    # for i in range(32):
        siblingCost = []
        siblingIndices = getSiblingIndices(nextData)
        progress += 1

        for index in siblingIndices:
            siblingCost.append(cost(nextArray, index, path, desiredArray))
        
        # printSiblingCost(siblingIndices, siblingCost)
        savedPath = path

        enque(nextArray, siblingIndices, siblingCost, queue, path)
        nextData = queue.pop(0)
        nextArray = nextData['sequence']
        path = nextData['path']

        printArrayWithProgress(nextArray, progress, path)

    printSuccess(progress)

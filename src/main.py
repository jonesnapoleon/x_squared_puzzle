from utils import printFail, printSuccess, printTime
from utils import fileToIntArray, setupOutputFile, desiredOutput
from rule import isReachable, getSiblingIndices, cost, decideNextArray, enque, printArrayWithWalkthrough
from datetime import datetime


start_time = datetime.now()
setupOutputFile()
array = fileToIntArray()
desiredArray = desiredOutput(array)

if not isReachable(array):
    printFail()
else:
    nextArray = [num for num in array]
    path = 0
    nextData = {'sequence': nextArray, 'cost': 0, 'prevAction': '', 'path': path, 'walkThrough': ''}
    progress = 0
    queue = []

    while nextArray != desiredArray:
        siblingCost = []
        siblingIndices = getSiblingIndices(nextData)

        for index in siblingIndices:
            siblingCost.append(cost(nextArray, index, path, desiredArray))
        
        enque(nextData, siblingIndices, siblingCost, queue, path)

        nextData = queue.pop(0)
        nextArray = nextData['sequence']
        path = nextData['path']
        progress += 1

    printArrayWithWalkthrough(array, nextData['walkThrough'])
    printSuccess(progress)

end_time = datetime.now()
printTime(str(start_time), str(end_time))
from utils import EMPTY, FILE_OUTPUT, printKurang, desiredOutput
from math import sqrt

def kurang(array, number):    
    index = array.index(number)

    if number != 0:
        count = 0        
        for i in range(index + 1, len(array)):
            if array[i] < number and array[i] != EMPTY:
                count += 1
        return count

    else:
        return len(array) - index - 1


def isReachable(array):
    
    x = int(isArsired(array))
    print(x)
    kurangSigma = 0

    for number in array:
        satuSigma = kurang(array, number)
        kurangSigma += satuSigma

    printKurang(kurangSigma + x)
    return (x + kurangSigma) % 2 == 0


def isArsired(array):
    index = array.index(EMPTY)
    gameSize = int(sqrt(len(array) + 1))

    i = int(index / gameSize)
    j = int(index % gameSize)

    return (i + j) % 2 == 1


def getSiblingIndices(data):
    array = data['sequence']
    index = array.index(EMPTY)
    gameSize = int(sqrt(len(array) + 1))
    sibling = []

    if index == 0:
        sibling = [index + 1, index + gameSize]
    elif index == gameSize - 1:
        sibling = [index - 1, index + gameSize]
    elif index == len(array) - 1:
        sibling = [index - gameSize, index - 1]
    elif index == len(array) - gameSize:
        sibling = [index - gameSize, index + 1]
    elif index < gameSize:
        sibling = [index - 1, index + 1, index + gameSize]
    elif index > len(array) - gameSize:
        sibling = [index - gameSize, index - 1, index + 1]
    elif index % gameSize == 0:
        sibling = [index - gameSize, index + 1, index + gameSize]
    elif (index + 1) % gameSize == 0:
        sibling = [index - gameSize, index - 1, index + gameSize]
    else:
        sibling = [index - gameSize, index - 1, index + 1, index + gameSize]

    if data['prevAction'] == 'DOWN':
        sibling.remove(index - gameSize)
    if data['prevAction'] == 'UP':
        sibling.remove(index + gameSize)
    if data['prevAction'] == 'LEFT':
        sibling.remove(index + 1)
    if data['prevAction'] == 'RIGHT':
        sibling.remove(index - 1)

    return sibling


def swapped(array, emptyIndex, index):
    swappedArray = [num for num in array]
    temp = swappedArray[emptyIndex]
    swappedArray[emptyIndex] = swappedArray[index]
    swappedArray[index] = temp
    return swappedArray


def cost(array, index, path, desiredArray):
    emptyIndex = array.index(EMPTY)
    count = 0
    swappedArray = swapped(array, emptyIndex, index)
    for i in range(len(swappedArray)):
        if(swappedArray[i] != desiredArray[i] and swappedArray[i] != EMPTY):
            count += 1
    return count + path


def decideNextArray(array, siblingIndices, siblingCost):

    # f = open(FILE_OUTPUT, "a+")
    # for i in siblingCost:
    #     f.write(str(i)+" ")
    # f.write("\n")
    emptyIndex = array.index(EMPTY)
    minim = min(siblingCost)
    indexToBeSwapped = siblingIndices[siblingCost.index(minim)]

    temp = array[emptyIndex]
    array[emptyIndex] = array[indexToBeSwapped]
    array[indexToBeSwapped] = temp


def enque(array, siblingIndices, siblingCost, queue, path):
    emptyIndex = array.index(EMPTY)
    gameSize = int(sqrt(len(array) + 1))

    for i in range(len(siblingIndices)):
        sequence = swapped(array, emptyIndex, siblingIndices[i])
        if(siblingIndices[i] - emptyIndex == gameSize):
            prevAction = "DOWN"
        if(siblingIndices[i] - emptyIndex == gameSize * -1):
            prevAction = "UP"
        if(siblingIndices[i] - emptyIndex == 1):
            prevAction = "RIGHT"
        if(siblingIndices[i] - emptyIndex == -1):
            prevAction = "LEFT"
        
        data = {
            'sequence': sequence,
            'cost': siblingCost[i],
            'prevAction': prevAction,
            'path': path + 1
        }
        # print(data)
        # f = open(FILE_OUTPUT, "a+")
        # for x in data['sequence']:
        #     f.write(str(x)+" ")
        # f.write("\n")
        if len(queue) == 0:
            queue.append(data)
        elif sequenceExist(queue, sequence):
            continue
        else:
            for j in range(len(queue)):                
                if j == len(queue) - 1:
                    queue.append(data)                    
                elif siblingCost[i] < queue[j]['cost']:
                    queue.insert(j, data)
                    break


def sequenceExist(queue, sequence):
    for val in queue:
        if val['sequence'] == sequence:
            return True
    return False

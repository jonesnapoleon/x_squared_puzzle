from utils import EMPTY, FILE_OUTPUT, printKurang
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


def siblingIndices(array):
    index = array.index(EMPTY)
    gameSize = int(sqrt(len(array) + 1))

    if index == 0 or index == gameSize - 1:
        return [index + 1, index + gameSize]
    elif index == len(array) - 1 or index == len(array) - gameSize:
        return [index - gameSize, index - 1]
    elif index < gameSize:
        return[index - 1, index + 1, index + gameSize]
    elif index > len(array) - gameSize:
        return[index - gameSize, index - 1, index + 1]
    elif index % gameSize == 0:
        return[index - gameSize, index + 1, index + gameSize]
    elif (index + 1) % gameSize == 0:
        return[index - gameSize, index - 1, index + gameSize]
    else:
        return[index - gameSize, index - 1, index + 1, index + gameSize]




from math import sqrt
import numpy as np

FILE_NAME = "file/input2.txt"
EMPTY = 0
FILE_OUTPUT = FILE_NAME.replace("in", "out")


def setupOutputFile():
    f = open(FILE_OUTPUT, "w")
    f.write("X-Squared Puzzle Game by Jones Napoleon\n")
    f.write("=========-------=======================\n")


def fileToIntArray():
    f = open(FILE_NAME, "r")
    array = f.read().replace('\n', " ").split(" ")
    array = list(map(lambda x: int(x), array))
    printInputArray(array)
    return array


def printInputArray(array):
    gameSize = int(sqrt(len(array) + 1))

    print("\nInput matrix")
    print("============")
    for i in range(len(array)):
        if((i+1) % gameSize == 0):
            print(array[i])
        else:
            print(array[i], end=' ')
    print("============\n")
    
    f = open(FILE_OUTPUT, "a+")

    f.write("\nInput matrix\n")
    f.write("============\n")
    for i in range(len(array)):
        if((i+1) % gameSize == 0):
            f.write(str(array[i]))
            f.write('\n')
        else:
            f.write(str(array[i]))
            f.write(' ')
    f.write("============\n")
    f.close()


def printArrayWithProgress(array, i):
    
    gameSize = int(sqrt(len(array) + 1))

    print("\nMatrix after progress-", i)
    print("============")
    for i in range(len(array)):
        if((i+1) % gameSize == 0):
            print(array[i])
        else:
            print(array[i], end=' ')
    print("============\n")
    
    f = open(FILE_OUTPUT, "a+")

    f.write("\nMatrix after progress-")
    f.write(str(i)+"\n")
    f.write("============\n")
    for i in range(len(array)):
        if((i+1) % gameSize == 0):
            f.write(str(array[i]))
            f.write('\n')
        else:
            f.write(str(array[i]))
            f.write(' ')
    f.write("============\n")
    f.close()


def printFail():
    print("Decision")
    print("=========")
    print("This puzzle cannot be solved!\n")

    f = open(FILE_OUTPUT, "a+")

    f.write("\nDecision\n")
    f.write("=========\n")
    f.write("This puzzle cannot be solved!\n")


def arrayToMatrix(array):
    length = int(sqrt(len(array) + 1))
    breadth = length
    count = 0
    matrix = []
    for i in range(length):
        a = []
        for j in range(breadth):
            a.append(array[count])
            count += 1
        matrix.append(a)
    
    return matrix


def matrixToArray(matrix):
    return np.array(matrix).ravel()


def printKurang(totalSigma):

    print("Fungsi Kurang(i)")
    print("================")
    print(totalSigma, '\n')

    f = open(FILE_OUTPUT, "a+")
    f.write("\nFungsi Kurang(i)\n")
    f.write("================\n")
    f.write(str(totalSigma))
    f.write('\n')

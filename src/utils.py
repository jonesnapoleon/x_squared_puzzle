from math import sqrt
import numpy as np

FILE_NAME = "file/input.txt"
EMPTY = 0
FILE_OUTPUT = FILE_NAME.replace("in", "out")


def setupOutputFile():
    f = open(FILE_OUTPUT, "w")
    f.write("X-Squared Puzzle Game by Jones Napoleon\n")
    f.write("=======================================\n")


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
    print("======\n")
    
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
    f.write("============\n\n")
    f.close()


def printArrayWithProgress(array, i, batch):
    inString = str(i)
    gameSize = int(sqrt(len(array) + 1))

    print("Matrix after progress", i, 'from batch', batch)
    print("======================================")
    for i in range(len(array)):
        if((i+1) % gameSize == 0):
            print(array[i])
        else:
            print(array[i], end=' ')
    print("=====\n")

    f = open(FILE_OUTPUT, "a+")

    f.write("\nMatrix after progress ")
    f.write(inString+" from batch "+str(batch)+"\n")
    f.write("====================================\n")
    for i in range(len(array)):
        if((i+1) % gameSize == 0):
            f.write(str(array[i]))
            f.write('\n')
        else:
            f.write(str(array[i]))
            f.write(' ')
    f.write("=====\n")
    f.close()


def printFail():
    print("Decision")
    print("=========")
    print("This puzzle cannot be solved!")
    print("=========\n")
    
    f = open(FILE_OUTPUT, "a+")

    f.write("\nDecision\n")
    f.write("=========\n")
    f.write("This puzzle cannot be solved!\n")
    f.write("=========\n")


def printSuccess(progress):
    print("Decision")
    print("=========")
    print("This puzzle is solved after progress "+str(progress)+"!")
    print("=========\n")

    f = open(FILE_OUTPUT, "a+")
    f.write("\nDecision\n")
    f.write("=========\n")
    f.write("This puzzle is solved after progress "+str(progress)+"!\n")
    f.write("=========\n")


def desiredOutput(array):
    length = len(array)
    desiredArray = [(i + 1) for i in range(length)]
    desiredArray[length - 1] = 0
    return desiredArray


def printKurang(totalSigma):
    print("Sigma Fungsi Kurang + X ->", totalSigma, '\n')
    f = open(FILE_OUTPUT, "a+")
    f.write("Sigma Fungsi Kurang + X -> "+str(totalSigma)+"\n\n")


def printSatuKurang(satu, number):
    print("Fungsi Kurang("+str(number)+") ->", satu)
    f = open(FILE_OUTPUT, "a+")
    f.write("Fungsi Kurang("+str(number)+") -> "+str(satu)+"\n")


def printSiblingCost(arr, ar):
    f = open(FILE_OUTPUT, "a+")
    f.write("\nSibling index\n")
    f.write("================\n")
    for i in arr:
        f.write(str(i))
        f.write(" ")
    f.write('\n')

    f.write("Sibling cost\n")
    f.write("================\n")
    for i in ar:
        f.write(str(i))
        f.write(" ")
    f.write('\n')


def printTime(start, end):
    print(start)
    print(end)
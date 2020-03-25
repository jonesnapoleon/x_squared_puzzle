from math import sqrt
import datetime
import time

FILE_REPRESENTATIVE_EMPTY = '0'
EMPTY = 0
EMPTY_IN_STRING = str(EMPTY)
FOLDER = "file/" + "test"
FILE_NAME = FOLDER + "/input.txt"
FILE_OUTPUT = FILE_NAME.replace("in", "out")


def setupOutputFile():
    f = open(FILE_OUTPUT, "w")
    f.write("X-Squared Puzzle Game by Jones Napoleon\n")
    f.write("=======================================\n")


def fileToIntArray():
    print(FILE_NAME)
    f = open(FILE_NAME, "r")
    array = f.read().replace('\n', " ").replace(FILE_REPRESENTATIVE_EMPTY, EMPTY_IN_STRING).split(" ")
    print(array)
    array = list(map(lambda x: int(x), array))
    printInputArray(array)
    return array


def printInputArray(array):
    gameSize = int(sqrt(len(array) + 1))

    print("\nInput matrix")
    print("==============")
    for i in range(len(array)):
        if((i+1) % gameSize == 0):
            print(array[i])
        else:
            print(array[i], end=' ')
    print("==============\n")
    
    f = open(FILE_OUTPUT, "a+")

    f.write("\nInput matrix\n")
    f.write("==============\n")
    for i in range(len(array)):
        if((i+1) % gameSize == 0):
            f.write(str(array[i]))
            f.write('\n')
        else:
            f.write(str(array[i]))
            f.write(' ')
    f.write("==============\n\n")
    f.close()


def printArrayWithProgress(array, i, prevAction):
    inString = str(i)
    gameSize = int(sqrt(len(array) + 1))

    print("Matrix after progress", i)
    print("========================")
    print("Last move:", prevAction)
    print("========================")
    for i in range(len(array)):
        if((i+1) % gameSize == 0):
            print(array[i])
        else:
            print(array[i], end=' ')
    print("==============\n")

    f = open(FILE_OUTPUT, "a+")

    f.write("\nMatrix after progress ")
    f.write(inString+"\n")
    f.write("========================\n")
    f.write("Last move: "+prevAction+"\n")
    f.write("========================\n")
    for i in range(len(array)):
        if((i+1) % gameSize == 0):
            f.write(str(array[i]))
            f.write('\n')
        else:
            f.write(str(array[i]))
            f.write(' ')
    f.write("==============\n")
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
    print("This puzzle is solved after raising "+str(progress)+" nodes!") if progress != 0 else print("This puzzle is already solved!")
    print("=========\n")

    f = open(FILE_OUTPUT, "a+")
    f.write("\nDecision\n")
    f.write("=========\n")
    f.write("This puzzle is solved after raising "+str(progress)+" nodes!\n") if progress != 0 else f.write("This puzzle is already solved!\n")
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


def printTime(start, end):
    startsTime = start.split(' ')[1].split('.')
    [timeS, milisecS] = startsTime
    x = time.strptime(timeS, '%H:%M:%S')
    startTotal = float(datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds())
    milisecS = float(str('0.') + str(milisecS))

    endTime = end.split(' ')[1].split('.')
    [timeE, milisecE] = endTime
    y = time.strptime(timeE, '%H:%M:%S')
    endTotal = float(datetime.timedelta(hours=y.tm_hour,minutes=y.tm_min,seconds=y.tm_sec).total_seconds())
    milisecE = float(str('0.') + str(milisecE))
    
    timeBefore = startTotal + milisecS    
    timeAfter = endTotal + milisecE
    delta = (timeAfter - timeBefore)

    print("Execution time")
    print("==============")
    print(delta, 'seconds')
    print("==============\n")


    f = open(FILE_OUTPUT, "a+")
    f.write("\nExecution time\n")
    f.write("==============\n")
    f.write(str(delta))
    f.write(" seconds\n")
    f.write("==============\n\n")


# Debug purposes
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

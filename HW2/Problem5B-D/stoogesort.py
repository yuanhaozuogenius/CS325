from random import randint
import timeit

def genRandomNumbers(numToGen):
    numArray = []

    for x in xrange(0,numToGen):
        numArray.append(randint(0,10000))

    return numArray


def stooge_sort(array, low_index, high_index):
    n = high_index - low_index + 1

    if n == 2 and array[low_index] > array[low_index + 1]:
        storage = array[low_index]
        array[low_index] = array[low_index + 1]
        array[low_index + 1] = storage
    elif n > 2:
        m = int(math.ceil(2 * float(n) / 3))
        stooge_sort(array, low_index, m - 1 + low_index)
        stooge_sort(array, n - m + low_index, high_index)
        stooge_sort(array, low_index, m - 1 + low_index)


timeArray = (1000,2000,5000,10000,20000,30000,35000)

outFile = open("stoogetime.csv", "w")

outFile.write("num,time\n")

for num in timeArray:
    for x in xrange(0,5):
        randomArray = genRandomNumbers(num)
        start_time = timeit.default_timer()
        stooge_sort(randomArray)
        elapsed = timeit.default_timer() - start_time

        outFile.write(str(num) + "," + str(elapsed) + '\n')

outFile.close()

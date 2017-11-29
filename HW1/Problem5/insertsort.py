from random import randint
import timeit

def genRandomNumbers(numToGen):
	numArray = []

	for x in xrange(0,numToGen):
		numArray.append(randint(0,10000))

	return numArray

def insertionSort(array):
	for j in xrange(1,len(array)):
		key = array[j]

		i = j - 1
		while (i > -1) and (array[i] > key):
			array[i + 1] = array[i]
			i = i - 1

		array[i + 1] = key

timeArray = (1000,2000,5000,10000,20000,30000,35000)

outFile = open("inserttime.csv", "w")

outFile.write("num,time\n")

for num in timeArray:
	for x in xrange(0,5):
		randomArray = genRandomNumbers(num)
		start_time = timeit.default_timer()
		insertionSort(randomArray)
		elapsed = timeit.default_timer() - start_time

		outFile.write(str(num) + "," + str(elapsed) + '\n')

outFile.close()

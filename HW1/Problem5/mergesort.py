from random import randint
import timeit

def genRandomNumbers(numToGen):
	numArray = []

	for x in xrange(0,numToGen):
		numArray.append(randint(0,10000))

	return numArray

def mergeSort(array):
	arraySize = len(array)

	if arraySize == 1 or arraySize == 0:
		return array

	arraySplit = arraySize / 2

	n1 = mergeSort(array[:arraySplit])
	n2 = mergeSort(array[arraySplit:])
	
	return merge(n1, n2)

def merge(array1, array2):
	newArray = []

	while len(array1) != 0 and len(array2) != 0:

		if array1[0] < array2[0]:
			newArray.append(array1.pop(0))
		else:
			newArray.append(array2.pop(0))

	if len(array1) == 0:
		newArray += array2
	else:
		newArray += array1

	return newArray

timeArray = (1000,2000,5000,10000,20000,30000,35000)

outFile = open("mergetime.csv", "w")

outFile.write("num,time\n")

for num in timeArray:
	for x in xrange(0,5):
		randomArray = genRandomNumbers(num)
		start_time = timeit.default_timer()
		sortedArray = mergeSort(randomArray)
		elapsed = timeit.default_timer() - start_time

		outFile.write(str(num) + "," + str(elapsed) + '\n')

outFile.close()

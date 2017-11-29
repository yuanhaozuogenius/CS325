def insertionSort(array):
	for j in xrange(1,len(array)):
		key = array[j]

		i = j - 1
		while (i > -1) and (array[i] > key):
			array[i + 1] = array[i]
			i = i - 1

		array[i + 1] = key

dataFile = open("data.txt", "r");
outFile = open("insert.out", "w");

for line in dataFile:
    lineArray = list(map(int,line.split()))

    intArray = lineArray[1:]

    insertionSort(intArray)

    for char in intArray:
        outFile.write(str(char) + ' ')

    outFile.write('\n')

dataFile.close()
outFile.close()
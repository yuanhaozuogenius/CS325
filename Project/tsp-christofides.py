# class Graph:
#     def __init__(nodes):
#         self.nodes = nodes
#
#     def add_node(index, x_coord, y_coord):
#
#
#     def calculate_distances():
#
# class Node:
#     def __init__(index, x_coord, y_coord):
#         self.index = index
#         self.x_coord = x_coord
#         self.y_coord = y_coord

dataFile = open("test-input-1.txt", "r");
outFile = open("test-input-1-solutions", "w");

nodes = []

for line in dataFile:
    lineArray = list(map(int,line.split()))

    coords = lineArray[1:]
    nodes.append(coords)

    # insertionSort(intArray)
    #
    # for char in intArray:
    #     outFile.write(str(char) + ' ')

    outFile.write('\n')

print(nodes)

dataFile.close()
outFile.close()

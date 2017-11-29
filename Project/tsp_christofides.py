"""This module creates a graph from an input file in order to do TSP
calculations using the Christofides Algorithm"""

import math

def calc_distance(x_coord1, y_coord1, x_coord2, y_coord2):
    """Calculates the distance between two points with given coordinates"""
    distance = math.sqrt((x_coord2-x_coord1)**2+(y_coord2-y_coord1)**2)
    return distance

class Graph(object):
    """Class that defines a graph for TSP problem"""
    def __init__(self):
        self.nodes = []

    def add_node(self, x_coord, y_coord):
        """Adds a node to the graph"""
        self.nodes.append([x_coord, y_coord, []])

    def populate_distances(self):
        """Adds distances to every other node on each node of the graph"""
        for i in range(0, len(self.nodes)):
            for j in range(0, len(self.nodes)):
                x_coord1 = self.nodes[i][0]
                y_coord1 = self.nodes[i][1]
                x_coord2 = self.nodes[j][0]
                y_coord2 = self.nodes[j][1]
                distance = calc_distance(x_coord1, y_coord1, x_coord2, y_coord2)
                self.nodes[i][2].append(distance)

    def print_nodes(self):
        """Show all of the nodes of the graph"""
        for node in self.nodes:
            print(node)

def main():
    """Main function"""
    graph = Graph()

    data_file = open("test-input-1.txt", "r")
    out_file = open("test-input-1-solutions", "w")

    for line in data_file:
        line_array = list(map(int, line.split()))

        coords = line_array[1:]
        x_coord = coords[0]
        y_coord = coords[1]

        graph.add_node(x_coord, y_coord)

        out_file.write('\n')

    graph.populate_distances()
    graph.print_nodes()

    data_file.close()
    out_file.close()

if __name__ == "__main__":
    main()

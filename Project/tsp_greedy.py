"""
This module creates a graph from an input file in order to do TSP
calculations using the Christofides Algorithm

Written by:
Samantha Manubay
Prathik Sannecy
Christian Mello
"""

import math
import sys


def greedy_algorithm(list_of_cities):
    """Solves TSP using the greedy algorithm and returns the tour"""

    # this will hold the shortest tour
    shortest_tour_route = []

    # this var will hold the shortest tour's distance
    shortest_tour_distance = sys.maxsize

    for i in range(0, len(list_of_cities) - 1):

        # start with the first city in the list of cities
        tour = [list_of_cities[i]]

        # create a list from the remaining cities
        remaining_cities = list_of_cities[:i + 0] + list_of_cities[i + 1:]

        # var to hold running total distance
        total_distance = 0

        # while list of remaining cities is not empty
        while remaining_cities:

            # city id with shortest_distance
            shortest_distance_id = 0

            # make the shortest_distance default to something ridiculously huge to start
            shortest_distance = sys.maxsize

            # find in remaining_cities one with shortest distance to current shortest_distance_id
            for j in remaining_cities:

                # define the coordinates
                x1_coord = j[0]
                x2_coord = tour[-1][0]
                y1_coord = j[1]
                y2_coord = tour[-1][1]

                # calculate result as per the distance formula
                distance = math.sqrt((x1_coord - x2_coord)
                                     ** 2 + (y1_coord - y2_coord) ** 2)

                # round the result
                distance = int(round(distance))

                # if shorter distance is found
                if distance < shortest_distance:

                    # update city id with shortest_distance
                    shortest_distance_id = j

                    # update shortest_distance with found distance
                    shortest_distance = distance

            # add shortest_distance to running total
            total_distance += shortest_distance

            # add city id with shortest_distance to the end of the current tour
            tour.append(shortest_distance_id)

            # pop the previously selected city from the list
            remaining_cities.remove(shortest_distance_id)

        # return path
        x1_coord = tour[0][0]
        x2_coord = tour[-1][0]
        y1_coord = tour[0][-1]
        y2_coord = tour[-1][1]

        total_distance += int(round(math.sqrt((x1_coord - x2_coord)
                                              ** 2 + (y1_coord - y2_coord) ** 2)))

        # creating a list to hold the tour_city_ids
        tour_city_ids = []

        for j in tour:
            # add the city ids to the list
            index = [l for l, n in enumerate(list_of_cities) if n == j]

            for k in index:
                if k not in tour_city_ids:
                    tour_city_ids.append(k)

            if len(index) > 1:
                pass

        # if the total_distance of this tour is shorter, update
        if total_distance < shortest_tour_distance:
            shortest_tour_distance = total_distance
            shortest_tour_route = tour_city_ids

    # temp print results to screen
    print(shortest_tour_distance)
    print(shortest_tour_route)

    # return the list
    return shortest_tour_distance, shortest_tour_route


def main():
    """Takes an input file from the command line and runs a greedy algorithm to
    solve the Travelling Salesman Problem"""

    data_filename = sys.argv[1]
    data_file = open(data_filename, "r")
    out_filename = data_filename + ".tour"
    out_file = open(out_filename, "w")

    list_of_cities = []

    for line in data_file:
        # split data into a graph
        line_array = list(map(int, line.split()))

        # add the last two line columns to coords
        coords = line_array[1:]

        # add these coords to list of cities
        list_of_cities.append(coords)

    # send list to greedy_algorithm function and get tour list in return
    total_distance, test_input_solution = greedy_algorithm(list_of_cities)

    # write to file the total distance
    out_file.write('%s \n' % total_distance)

    for line in test_input_solution:
        # write to file the city ids in order of visitation
        out_file.write('%s \n' % line)

    data_file.close()
    out_file.close()


if __name__ == "__main__":
    main()

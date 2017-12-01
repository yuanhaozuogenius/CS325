"""
This module creates a graph from an input file in order to do TSP
calculations using the Greedy Algorithm
Written by:
Samantha Manubay
Prathik Sannecy
Christian Mello
"""

import math
import sys

def compute_distance(x1, x2, y1, y2):
    '''Computes the distance formula and rounds result after accepting the necessary variables'''

    # calculate result as per the distance formula
    computed_distance = math.sqrt((x1 - x2) ** 2 + ((y1 - y2) ** 2))

    # round the result
    computed_distance = int(round(computed_distance))

    return computed_distance

def greedy_algorithm(list_of_cities):
    """Solves TSP using the greedy algorithm and returns the tour"""

    # this will hold the shortest tour
    shortest_tour_route = []

    # this var will hold the shortest tour's distance
    shortest_tour_distance = sys.maxsize

    # get length of list_of_cities
    city_list_range = len(list_of_cities) - 1

    # generate list of cities to iterate through
    for i in range(0, city_list_range):

        # start with the first city in the list of cities
        tour = [list_of_cities[i]]

        # remaining cities = beginning of list up to i + items after i
        remaining_cities = list_of_cities[:i] + list_of_cities[i + 1:]

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

                # get the rounded distance per the distance formula
                distance = compute_distance(j[0], tour[-1][0], j[1], tour[-1][1])

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

        #return path
        total_distance += compute_distance(tour[0][0], tour[-1][0], tour[0][-1], tour[-1][1])

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

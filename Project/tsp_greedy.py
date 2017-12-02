"""
This module creates a graph from an input file in order to do TSP
calculations using the Greedy Algorithm
Written by:
Samantha Manubay
Prathik Sannecy
Christian Mello
"""



from math import sqrt
import sys

def IsFileBig(data_file_name):
    data_file = open(data_file_name, "r")
    size=sum(1 for _ in data_file)
    data_file.close()
    if size > 300:
       return True
    return False


def compute_distance(x1, x2, y1, y2):
    '''Computes the distance formula and rounds result after accepting the necessary variables'''

    # calculate result as per the distance formula
    computed_distance = sqrt((x1 - x2) ** 2 + ((y1 - y2) ** 2))

    # round the result
    computed_distance = int(round(computed_distance))

    return computed_distance



def greedy_algorithm_fast(list_of_cities, outFile):

    # start with the first city in the list of cities
    tour = [list_of_cities[0]]

    # create a list from the remaining cities
    remaining_cities = list_of_cities[1:]

    # var to hold running total distance
    total_distance = 0

    # while list of remaining cities is not empty
    while remaining_cities:

        # city id with shortest_distance
        shortest_distance_id = 0

        # make the shortest_distance default to something ridiculously huge to start
        shortest_distance = sys.maxsize

        # find in remaining_cities one with shortest distance to current shortest_distance_id
        for i in remaining_cities:

            # define the coordinates
            x1_coord = i[0]
            x2_coord = tour[-1][0]
            y1_coord = i[1]
            y2_coord = tour[-1][1]

            # calculate result as per the distance formula
            distance = compute_distance(x1_coord, x2_coord, y1_coord, y2_coord)

            # if shorter distance is found
            if (distance < shortest_distance):

                # update city id with shortest_distance
                shortest_distance_id = i

                # update shortest_distance with found distance
                shortest_distance = distance

        # add shortest_distance to running total
        total_distance += shortest_distance

        # add city id with shortest_distance to the end of the current tour
        tour.append(shortest_distance_id)

        # pop the previously selected city from the list
        remaining_cities.remove(shortest_distance_id)

    # creating a list to hold the tour_city_ids
    tour_city_ids = []

    # return path
    x1_coord = tour[0][0]
    x2_coord = tour[-1][0]
    y1_coord = tour[0][-1]
    y2_coord = tour[-1][1]

    total_distance += compute_distance(x1_coord, x2_coord, y1_coord, y2_coord)

    # creating a list to hold the tour_city_ids
    tour_city_ids = []

    # write to file the total distance
    outFile.write('%s \n' % total_distance)



    for j in tour:
        # add the city ids to the list
        index = [l for l, n in enumerate(list_of_cities) if n == j]

        for k in index:
            if k not in tour_city_ids:
                tour_city_ids.append(k)

        if len(index) > 1:
            pass
    # return the list
    return tour_city_ids


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
                
                # define the coordinates
                x1_coord = j[0]
                x2_coord = tour[-1][0]
                y1_coord = j[1]
                y2_coord = tour[-1][1]
                
                # get the rounded distance per the distance formula
                distance = compute_distance(x1_coord, x2_coord, y1_coord, y2_coord)

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

        # define the coordinates
        x1_coord = tour[0][0]
        x2_coord = tour[-1][0]
        y1_coord = tour[0][-1]
        y2_coord = tour[-1][1]
        
        # return path
        total_distance += compute_distance(x1_coord, x2_coord, y1_coord, y2_coord)

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

    out_filename = data_filename + ".tour"
    out_file = open(out_filename, "w")

    FAST = IsFileBig(data_filename)
    data_file = open(data_filename, "r")

    list_of_cities = []

    for line in data_file:
        # split data into a graph
        line_array = list(map(int, line.split()))

        # add the last two line columns to coords
        coords = line_array[1:]

        # add these coords to list of cities
        list_of_cities.append(coords)

    # send list to greedy_algorithm function and get tour list in return
    if FAST == False:
        total_distance, test_input_solution = greedy_algorithm(list_of_cities)

        # write to file the total distance
        out_file.write('%s \n' % total_distance)

        print(test_input_solution)
        for line in test_input_solution:
            # write to file the city ids in order of visitation
            out_file.write('%s \n' % line)
    else:
        # send list to greedy_algorithm function and get tour list in return
        test_input_solution = greedy_algorithm_fast(list_of_cities, out_file)

        for line in test_input_solution:
            # write to file the city ids in order of visitation
            out_file.write('%s \n' % line)

    data_file.close()
    out_file.close()


if __name__ == "__main__":
    main()

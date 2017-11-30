import math
import sys


def greedy_algorithm(list_of_cities):
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
            for i in remaining_cities:

                # define the coordinates
                x1_coord = i[0]
                x2_coord = tour[-1][0]
                y1_coord = i[1]
                y2_coord = tour[-1][1]

                # calculate result as per the distance formula
                distance = math.sqrt(math.pow(x1_coord - x2_coord, 2) + math.pow(y1_coord - y2_coord, 2))

                # round the result
                distance = int(round(distance))

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

        # return path
        x1_coord = tour[0][0]
        x2_coord = tour[-1][0]
        y1_coord = tour[0][-1]
        y2_coord = tour[-1][1]

        total_distance += int(round(math.sqrt(math.pow(x1_coord - x2_coord, 2) + math.pow(y1_coord - y2_coord, 2))))

        # creating a list to hold the tour_city_ids
        tour_city_ids = []



        for i in tour:
            # add the city ids to the list
            tour_city_ids.append(list_of_cities.index(i))

        # if the total_distance of this tour is shorter, update
        if (total_distance < shortest_tour_distance):
            shortest_tour_distance = total_distance
            shortest_tour_route = tour_city_ids

    # temp print results to screen
    print(shortest_tour_distance)
    print(shortest_tour_route)

    # return the list
    return shortest_tour_distance, shortest_tour_route


dataFile = open("tsp_example_1.txt", "r");
outFile = open("tsp_example_1_solutions.txt", "w");

list_of_cities = []

for line in dataFile:
    # split data into a graph
    lineArray = list(map(int, line.split()))

    # add the last two line columns to coords
    coords = lineArray[1:]

    # add these coords to list of cities
    list_of_cities.append(coords)

# send list to greedy_algorithm function and get tour list in return
total_distance, test_input_solution = greedy_algorithm(list_of_cities)
# write to file the total distance
outFile.write('%s \n' % total_distance)
for line in test_input_solution:
    # write to file the city ids in order of visitation
    outFile.write('%s \n' % line)

dataFile.close()
outFile.close()

import math


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


def main():
    data_file = open("data.txt", "r")
    out_file = open("stooge.out", "w")

    for line in data_file:
        line_array = list(map(int, line.split()))

        int_array = line_array[1:]

        stooge_sort(int_array, 0, len(int_array) - 1)

        for char in int_array:
            out_file.write(str(char) + ' ')

        out_file.write('\n')

    data_file.close()
    out_file.close()


if __name__ == "__main__":
    main()

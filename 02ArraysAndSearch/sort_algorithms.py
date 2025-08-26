class SortAlgorithms:
    def __init__(self, array):
        self.array = array

    # Bubble Sort
    def bubble_sort(self):
        array = self.array.copy()
        length_of_array = len(array)

        for i in range(length_of_array):
            for j in range(0, length_of_array - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array

    # Insertion Sort
    def insertion_sort(self):
        array = self.array.copy()
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array

    # Selection Sort
    def selection_sort(self):
        array = self.array.copy()
        length_of_array = len(array)
        for i in range(length_of_array):
            min_index = i
            for j in range(i + 1, length_of_array):
                if array[j] < array[min_index]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]
        return array


# Main program
if __name__ == "__main__":
    data = [64, 85, 11, 21, 5]
    sort_algorithms = SortAlgorithms(data)

    print("Original Data:", data)
    print("Bubble Sort:", sort_algorithms.bubble_sort())
    print("Insertion Sort:", sort_algorithms.insertion_sort())
    print("Selection Sort:", sort_algorithms.selection_sort())
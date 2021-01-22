import random
import time

#Function that generates a random list with "numerus" elements (numbers 1-"numerus")

def random_list():
    my_list = []
    numerus = 10000
    for i in range(1, numerus + 1):
        n = random.randint(1, numerus)
        my_list.append(n)
    size = len(my_list)
    print("Size of List: ", size)
    #print("Unsorted List: ", my_list)
    return my_list

def selection_sort(my_list):
    # i indicates how many items were sorted
    for i in range(len(my_list)-1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(my_list)):
            # Update the min_index if the element at j is lower than it
            if my_list[j] < my_list[min_index]:
                min_index = j
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    #print("Selection Sorted List: ", my_list)

class Stopwatch:
    def __init__(self, msg=""):
        self.msg = msg

    def __enter__(self):
        self.start = time.time()
        return self

    def current(self):
        return time.time() - self.start

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.msg, self.current())


my_list = random_list()
with Stopwatch("Final Time: ") as stopwatch:
    selection_sort(my_list)
    stopwatch



#Wie Calle ich die Stopwatch class richtig?

#Time for sorting list of 100 elements: 2.032 seconds
#Time for sorting list of 100000 elements:
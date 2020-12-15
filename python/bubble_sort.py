def bubble_sort(list_sort):
    has_swapped = True
    num_of_iterations = 0
    while(has_swapped):
        has_swapped = False
        for i in range(len(list_sort) - num_of_iterations - 1):
            if list_sort[i] > list_sort[i+1]:
                list_sort[i], list_sort[i+1] = list_sort[i+1], list_sort[i]
                has_swapped = True
        num_of_iterations += 1
        return list_sort

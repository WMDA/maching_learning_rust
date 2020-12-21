def optimised_bubble_sort(l):
    for limit in reversed(range(0, len(l))):
        for i in range(0,limit):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
    return l

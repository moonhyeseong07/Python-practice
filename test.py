array = [2, 3, 1, 4]
def quick_sort(array):
    #quit if list has one or less elements
    if len(array) <= 1:
        return array
    
    pivot = array[0] # first element as pivot
    tail = array[1:] # list accept pivot
    left = [x for x in tail if x <= pivot] # left side
    right = [x for x in tail if x > pivot] # right side
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)
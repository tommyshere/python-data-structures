# linear search O(n)
def find_max(arr):
    max_num = array[0]
    for num in array:
        if num > max:
            max_num = num
    return max_num

def find_min(arr):
    min_num = array[0]
    for num in array:
        if num < max:
            min_num = num
    return min_num
    
# numpy is faster because it stores references of the object being stored

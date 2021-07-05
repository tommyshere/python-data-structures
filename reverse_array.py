# Reverse an array
def reverse_one(arr):
    temp_val = None
    end_index = len(arr) - 1
    for i in range(len(arr) // 2):
        temp_val = arr[end_index]
        arr[end_index] = arr[i]
        arr[i] = temp_val
        end_index -= 1
    return arr
    
def reverse_two(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
    
if __name__ == "__main__":
    print(reverse_one([1, 2, 3, 4, 5]))
    print(reverse_two([1, 2, 3, 4, 5]))
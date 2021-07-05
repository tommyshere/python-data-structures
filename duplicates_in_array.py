from collections import Counter

def one(arr):
    value = Counter(arr)
    for key in value:
        if value[key] > 1:
            return "DUPLICATES"
    return "NO DUPLICATES"
    
# this way only works if the values in the array are less than len(arr)
def two(arr):
    for num in arr:
        # if the value is positive, it is not a duplicate
        if arr[abs(num)] >= 0:
            # so it will change the value to a negative
            nums[abs(num)] = -nums[abs(num)]
        # but if it's a negative value, it has been switched and must negative!
        else:
            return "DUPLICATE"

if __name__ == "__main__":
    print(one([1, 2, 3, 1, 5]))
    print(two([1, 2, 3, 1, 5]))
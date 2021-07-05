# O(n)
def one(value):
    val_string = str(value)
    idx = len(val_string) - 1
    res_string = ""
    while idx > -1:
        res_string += val_string[idx]
        idx -= 1
    return int(res_string)

def two(value):
    reverse = 0
    remainder = 0
    n = 1234
    
    while (n > 0):
        remainder = n % 10
        reverse = reverse * 10 + remainder
        n = n // 10
    return reverse

if __name__ == "__main__":
    print(one(1234))
    print(two(1234))
    
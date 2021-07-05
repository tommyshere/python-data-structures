from collections import Counter

def one(param1, param2):
    if len(param1) != len(param2):
        return False
    # Counter is O(n)
    dict1 = Counter(param1.lower())
    dict2 = Counter(param2.lower())
    if dict1[key] != dict2.get(key, None):
        return False
    return True


def two(param1, param2):
    if len(param1) != len(param2):
        return False
    # sorted has O(n log n)
    str1 = sorted(param1.lower())
    str2 = sorted(param2.lower())
    
    for i in range(len(param1)):
        if str1[i] != str2[i]:
            return False
    
    return True

if __name__ == "__main__":
    print(one("restful", "fluster"))
    print(two("restful", "fluster"))
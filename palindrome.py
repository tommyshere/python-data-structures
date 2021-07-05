def is_palindrome(input_val):
    start = 0
    end = len(input_val) - 1
    while start < end:
        if input_val[start] == input_val[end]:
            start += 1
            end -= 1
        else:
            return False  
    return True

if __name__ == "__main__":
    print(is_palindrome("madam"))
# reverse a linked list

def reverse():
    curr = head
    prev = None
    temp = None
    while curr:
        # set the variables first so it doesn't get overwritten
        temp = curr.next
        curr.next = prev
        prev = curr
        # don't forget about curr moving forward
        curr = temp
    
    head = None
        
# it's all about pointing back to prev
# 1 -> 2 -> 3
# None <- 1  2 -> 3
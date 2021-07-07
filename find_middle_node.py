# in-place to find middle node
# assume class Node is already implemented

def find_middle_node():
    slow = linkedList.head
    fast = linkedList.head
    
    if slow.next is None:
        return
        
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow
        
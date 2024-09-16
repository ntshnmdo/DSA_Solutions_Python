def rotateByK(self, head, k):
    if head == None:
        return head
    
    len = 1

    newH = tail = head

    while tail.next != None:
        tail = tail.next
        len+=1

    tail.next = head

    k %= len
    
    for i in range(0, len-k):
        tail = tail.next
    newH = tail.next
    tail.next = None
    return newH
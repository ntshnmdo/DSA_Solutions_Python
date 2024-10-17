def printLL(head):
    newTemp = head

    while newTemp.next != None:
        print(newTemp.val, end = "->")
        newTemp = newTemp.next
    
printLL
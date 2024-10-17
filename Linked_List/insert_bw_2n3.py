def printLL(head):
    newTemp = head

    while newTemp.next != None:
        print(newTemp.val, end = "->")
        newTemp = newTemp.next
    
printLL(head)

def insert(head, insertValue, index):
    insertNode = Node(insertValue)
    i = 0

    temp = head

    while temp.next != None and i<=index:
        i+=1 
        if i == index:
            future = temp.next
            temp.next = insertNode
            insertNode.next = future
            break
        temp = temp.next
    printLL(head)

insert(head, 10, 2)
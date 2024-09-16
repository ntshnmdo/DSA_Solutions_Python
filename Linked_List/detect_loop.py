def detectLoop (self, head):
    # Floyd's Algorithm or Slow and Fast pointer approach
    
    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
        
    return False

 # Hashmap approach TC O(n) and SC O(n)_
    
    def detectLoop(self, head):
        
        count = set()
        
        curr = head 
        
        while curr is not None:
            if curr in count:
                return True
            count.add(curr)
            curr = curr.next
        return False
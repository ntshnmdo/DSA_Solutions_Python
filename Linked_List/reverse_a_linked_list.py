class Solution:
    def reverseList(self, head):
        # recursive aaporach:
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next  = None

        return newHead
        
        # Two pointer approach (Iteratively)
        # prev, curr = None, head

        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev
class Solution:
    def reverseList(self,head: ListNode) -> ListNode:
        # only for empty linked list
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

# newhead is just a dumb container
# each node can access next node, hence change the next of that, and can change the next of self.
# new head is passed from back to front.
# 1 ->2 -> NULL
# First Call at node 1
# head  = 1, newhead = 2 (from 2nd fn call)
# head.next.next i.e pointer (next) of the node returned to self
# second call at node 2
# newhead = head = 2
# returns 2

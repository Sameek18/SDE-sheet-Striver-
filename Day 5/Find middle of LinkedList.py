class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head.next==None: #check if LL consis of 1 node
            return head
        slow=head        #nitialize 2 pointers
        fast=head
        while fast and fast.next:   #increment slow by 1 and fast  by 2
            slow=slow.next
            fast=fast.next.next
        return slow

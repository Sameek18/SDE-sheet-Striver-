class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow=head   #initialize to pointers to head
        fast=head
        while fast and fast.next:
            fast=fast.next.next     #fast moves by 2
            slow=slow.next     #slow moves by one
            
            if slow==fast:
                              #if fast and slow meet inside loop return True   
                return True
        else:
            return False
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
          #initialize 2 nodes pointing to head
        slow=head
        fast=head
        isloop=False
        
           #checking if LL consists of 1-2 elements
        if head==None or head.next==None:
            return None
        
           #checking if there is a loop
        while fast and fast.next: 
            fast=fast.next.next
            slow=slow.next
            if slow==fast:      #if there is a loop then slow and fast will meet
                isloop=True
                break
                
                
            #find position where loop starts  
            #the point at which both pointers meet is the start of the loop
        if isloop:
            slow=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
                
            return fast
        
        
        return None
                

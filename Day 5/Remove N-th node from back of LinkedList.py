#two pointer approach

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #initialize two pointers pointing to head
        slow=head
        fast=head
        count=0
        #check if list is empty or has only 1 element
        
        if head==None or head.next==None:
            return None
        else:
            
            for i in range(n):      #set a difference of n nodes between slow and fast
                fast=fast.next  
        
            if not fast:              #check if n is greater than size of LL 
                return head.next
            
        #increment both pointers  
            while fast.next!=None:
                fast=fast.next
                slow=slow.next

            slow.next=slow.next.next  #delete node

        return head

    
       

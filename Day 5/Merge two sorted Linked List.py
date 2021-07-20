def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy =ListNode(-1)     #we will take a dummy node
        current=dummy           #current points to the dummy node 
        
        while(l1!=None and l2!=None): #comparing elements in both lists
            if l1.val<l2.val:       
                current.next=l1              #smaller node is connected to current node
                l1=l1.next
            else:
                current.next=l2
                l2=l2.next
            current=current.next
            
            
            #condition when one of the LL reaches Null 
        if l1!=None: 
            current.next=l1
        else:
            current.next=l2
            
        return dummy.next
#Using 2 pointer approach
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr is not None:
            head = curr.next
            curr.next = prev
            prev = curr
            curr = head
        return prev
    
    
    
#using a stack 

def reverseList(self, head: ListNode) -> ListNode:
        stack=[]
        temp=head
        #put all LL elements in stack
        while temp:
            stack.append(temp)
            temp=temp.next
        #pop elements prom stack and put back in LL  
        while len(stack)>0:
            elem=stack.pop()
            temp.next=elem
            temp=elem
            
        elem.next=None
            
        return head

#Naive method
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #initialize 2 empty strings
        s1=""
        s2=""
        n1=0
        n2=0
        i=0
        ans=[]
        
        #append values of LL l1 into string S1
        while l1:
            s1+=str(l1.val)
            l1=l1.next
            
        #append values of LL l2 into string S2
        while l2:
            s2+=str(l2.val)
            l2=l2.next
            
        #reverse the string and conver to int
            
        n1=int(s1[::-1])
        n2=int(s2[::-1])
        
        #add the two numers and conver to string and reverse it
        #put each digit in list
        ans=list(map(int,str(n1+n2)[::-1]))
        
        #declare new node
        
        dummy = curr =  ListNode(0)
        
        #create new node and add values of list
        for i in ans:
            curr.next = ListNode(val = int(i))
            curr = curr.next
        
        curr.next  = None
        return dummy.next
        



class Solution:
    def addTwoNumbers(self, root1: ListNode, root2: ListNode) -> ListNode:
        first=root1
        second=root2
        carry=0
        root=temp=node(0)
        while first or second:
            v1,v2=0,0
            if first:
                v1=first.data
                first=first.next
            if second:
                v2=second.data
                second=second.next
            sum1=v1+v2+carry
            if sum1>=10:
                carry=1
                sum1%=10
            else:
                carry=0
            temp.next=node(sum1)
            temp=temp.next
        if carry:
            temp.next=node(carry)
        return root.next

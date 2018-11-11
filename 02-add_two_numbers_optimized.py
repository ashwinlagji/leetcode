# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = None
        current = None
        carry = 0
        # iterate through the two lists 
        while(l1 !=None and l2!=None):
            
            total = l1.val+l2.val + carry
            carry = total // 10
            temp = ListNode(total % 10)
            if(head == None):
                head = temp
                current = temp
            else:
                current.next = temp
                current = temp
            l1 = l1.next
            l2 = l2.next
        
        if(l1 !=None):
            while(l1 !=None):
                total = l1.val + carry
                carry = total // 10
                temp = ListNode(total % 10)
                if(head == None):
                    head = temp
                    current = temp
                else:
                    current.next = temp
                    current = temp
                l1 = l1.next
        if(l2 !=None):
            while(l2 !=None):
                total = l2.val + carry
                carry = total // 10
                temp = ListNode(total % 10)
                if(head == None):
                    head = temp
                    current = temp
                else:
                    current.next = temp
                    current = temp
                l2 = l2.next
        if(carry!=0):
            temp = ListNode(carry % 10)
            current.next = temp
            current = temp
    
        return head
        
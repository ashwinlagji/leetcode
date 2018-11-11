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
        
        # create a copy of the NodeList
        
        list1 = copy.deepcopy(l1)
        list2 = copy.deepcopy(l2)
        
        # extract the number from NodeList
        num1=0
        num2=0
        multiplier = 1
        while(list1 !=None and list2!=None):
            num1 += list1.val * multiplier 
            num2 += list2.val * multiplier
            
            list1 = list1.next
            list2 = list2.next
            multiplier *= 10 
        
        if(list1 !=None):
            while(list1 !=None):
                num1 += list1.val * multiplier 

                list1 = list1.next
                multiplier *= 10 
        if(list2 !=None):
            while(list2 !=None):
                num1 += list2.val * multiplier 

                list2 = list2.next
                multiplier *= 10 
        
        # get sum of two numbers
        total = num1 + num2
        
        # get the NodeList of the total
        head = None
        current = None
        while total >= 0:
            
            r = total % 10
            if(head == None):
                temp = ListNode(r)
                current = temp
                head = current
            else:
                temp = ListNode(r)
                current.next = temp
                current = temp
            total = (total // 10)
            if(total == 0):
                break
        return head
        
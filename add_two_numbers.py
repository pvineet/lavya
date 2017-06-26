# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addNode(self,l1,l2,carry):
        while True: 
            if l1 == None and l2 == None:
                if carry == 1:
                    sum = carry
                else:
                    break
            elif l1 == None:
                sum = (l2.val+carry)%10
                _carry = (l2.val+carry)/10
            elif l2 == None:
                sum = (l1.val+carry)%10
                _carry = (l1.val+carry)/10
            else:
                sum = (l1.val + l2.val+carry)%10
                _carry = (l1.val+l2.val+carry)/10
            
            if l1 == None and l2 == None:
                _next = None
            elif l1 == None:
                _next = self.addNode(None,l2.next,_carry)
            elif l2 == None:
                _next = self.addNode(l1.next,None,_carry)
            else:
                _next = self.addNode(l1.next,l2.next,_carry)

            node = ListNode(sum)
            node.next = _next
            return node
    def printList(self,list):
        while True:
            if list.next == None:
                break
            self.printList(list.next)
            
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        while True: 
            carry = (l1.val+l2.val)/10
            sum = (l1.val + l2.val)%10
            #self.printList(l1)
            #self.printList(l2)
            if l1.next != None or l2.next != None or carry != 0:
                _next = self.addNode(l1.next,l2.next,carry)
            else:
                _next = None
            node = ListNode(sum)
            node.next = _next
            return node
        
        
            

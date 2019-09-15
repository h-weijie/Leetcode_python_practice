# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = l1
        while l1.next and l2.next:
            l1.val += l2.val
            l1 = l1.next
            l2 = l2.next
        if l1.next:
            l1.val += l2.val
        else:
            l1.val += l2.val
            l1.next = l2.next
        carry = 0
        l1 = result
        while l1.next:
            temp = l1.val + carry
            carry = temp // 10
            l1.val = temp % 10
            l1 = l1.next
        temp = l1.val + carry
        carry = temp // 10
        l1.val = temp % 10
        if carry:
            l1.next = ListNode(1)
        return result
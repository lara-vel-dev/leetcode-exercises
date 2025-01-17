'''
-- 83. Remove Duplicates from Sorted List --
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

Example:

original: 1 --> 1 --> 2
output: 1 --> 2
Input: head = [1,1,2]
Output: [1,2]

Constraints:
* The number of nodes in the list is in the range [0, 300].
* -100 <= Node.val <= 100
* The list is guaranteed to be sorted in ascending order.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        if fast == None:
            return None
        while fast:
            if slow.val == fast.val:
                slow.next = fast.next
                fast = slow.next
            else:
                slow = slow.next
                fast = fast.next
        return head

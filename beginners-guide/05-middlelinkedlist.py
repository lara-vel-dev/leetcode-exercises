'''
-- 876. Middle of the Linked List --

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example:
1 --> 2 --> [3] --> 4 --> 5
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Constraints:
* The number of nodes in the list is in the range [1, 100].
* 1 <= Node.val <= 100
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.length = 0
        self.arr = []

        while head is not None:
            self.arr.append(head)
            head = head.next
            self.length += 1

        return self.arr[self.length // 2]

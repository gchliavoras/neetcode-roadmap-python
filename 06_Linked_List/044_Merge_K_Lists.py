#Merge K Sorted Linked Lists
#You are given an array of k linked lists lists, where each list is sorted in ascending order.
#Return the sorted linked list that is the result of merging all of the individual linked lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
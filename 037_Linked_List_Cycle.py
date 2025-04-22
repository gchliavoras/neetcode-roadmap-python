#Linked List Cycle Detection
#Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
#There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.
#Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.
#Note: index is not given to you as a parameter.
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    def hasCycle(self, head) -> bool:
      slow, fast = head, head
      while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if fast and slow == fast:
          return True
      return False
      
    def create_linkedList(self, values: [list]):
      if not values:
        return None
      head = ListNode(values[0])
      current = head
      for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
#      current.next = head
      
      return head
      
if __name__ == "__main__":
  values = [-9, 3, 5, 7, 2]
  solution = Solution()
  #Create sample linked list with a cycle.
  head = solution.create_linkedList(values)
  
  #Check for cycle:
  print(solution.hasCycle(head))
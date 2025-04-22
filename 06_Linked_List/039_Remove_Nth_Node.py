#Remove Node From End of Linked List
#You are given the beginning of a linked list head, and an integer n.
#Remove the nth node from the end of the list and return the beginning of the list.

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class ListOperations:
  def create(self, values: [list]):
    if not values:
      return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
      current.next = ListNode(val)
      current = current.next
    return head

  def disp(self, head: 'ListNode') -> None:
    current = head
    values = []
    while current:
      values.append(str(current.val))
      current = current.next
    print(" -> ".join(values))
    
    
class Solution:
  def removeNthFromEnd(self, head: 'Optional[ListNode]', n: int):
    dummy = ListNode()
    dummy.next = head
    current, previous = dummy, dummy
    for i in range(n):
      current = current.next
    while current.next:
      current = current.next
      previous = previous.next
    previous.next = previous.next.next
    return dummy.next
  
if __name__ == "__main__":
  values = [z for z in range(5)]
  n = 5
  solution = Solution()
  listOps = ListOperations()
  #Create and display sample linked list.
  head = listOps.create(values)
  listOps.disp(head)
  #Remove Nth node:
  head = solution.removeNthFromEnd(head,n)
  #Display reordered list.
  listOps.disp(head)
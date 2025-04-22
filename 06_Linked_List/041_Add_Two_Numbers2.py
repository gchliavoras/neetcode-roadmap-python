#Add Two Numbers
#You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.
#The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.
#Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#Return the sum of the two numbers as a linked list.
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def addTwoNumbers(self, l1: 'Optional[ListNode]', l2: 'Optional[ListNode]') -> 'Optional[ListNode]':
    dummy = ListNode()
    current = dummy
    current1, current2 = l1, l2
    carry = 0
    while current1 or current2 or carry:
      total = 0
      if current1:
        total += current1.val
        current1 = current1.next
      if current2:
        total += current2.val
        current2 = current2.next
      total += carry
      
      if total > 9:
        total -= 10
        carry = 1
      else:
        carry = 0
        
      current.next = ListNode(total)
      current = current.next
      
    return dummy.next

def createList(values: [list]):
  if not values:
    return None
  head = ListNode(values[0])
  current = head
  for val in values[1:]:
    current.next = ListNode(val)
    current = current.next
  return head

def dispList(head: 'ListNode') -> None:
  current = head
  values = []
  while current:
    values.append(str(current.val))
    current = current.next
  print(" -> ".join(values))
    
if __name__ == "__main__":
  l1_data = [1]
  l2_data = [9, 9]
  l1 = createList(l1_data)
  l2 = createList(l2_data)
  
  print("List1:")
  dispList(l1)
  print("List2:")
  dispList(l2)
  
  sol = Solution()
  l3 = sol.addTwoNumbers(l1, l2)
  print("List3:")
  dispList(l3)
  
  
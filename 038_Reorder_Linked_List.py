#Reorder Linked List
#You are given the head of a singly linked-list.
#The positions of a linked list of length = 7 for example, can intially be represented as:
#[0, 1, 2, 3, 4, 5, 6]
#Reorder the nodes of the linked list to be in the following order:
#[0, 6, 1, 5, 2, 4, 3]
#Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
#[0, n-1, 1, n-2, 2, n-3, ...
#You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
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
  def reorderList(self, head: 'Optional[ListNode]') -> None:
    
    if not head or not head.next or not head.next.next:
      return

    current = head
    
    while current and current.next and current.next.next:
      
      previous = current
      tail = current.next
      while tail.next: #Go to last node.
        previous = tail
        tail = tail.next
      #Remove last node...  
      previous.next = None
      #... and insert after current.
      temp = current.next
      current.next = tail
      tail.next = temp
      current = tail.next
    
    return
    
if __name__ == "__main__":
  values = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  solution = Solution()
  listOps = ListOperations()
  #Create and display sample linked list.
  head = listOps.create(values)
  listOps.disp(head)
  #Reorder:
  solution.reorderList(head)
  #Display reordered list.
  listOps.disp(head)
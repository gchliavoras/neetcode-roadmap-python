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

    slow, fast = head, head
    #Go to middle of list.
    while fast.next and fast.next.next:
      slow = slow.next
      fast = fast.next.next
    #Seperate the list after the middle node.
    previous = slow.next
    current = previous.next
    slow.next = None
    previous.next = None
    #Reverse list after middle node.
    if not current:
      middleHead = previous
    else:
      while current.next:
        temp = current.next
        current.next = previous
        previous = current
        current = temp
      current.next = previous
      middleHead = current
    #Splice two lists:
    current = head
    while middleHead:
      temp1 = current.next
      temp2 = middleHead.next
      current.next = middleHead
      current = current.next
      current.next = temp1
      current = current.next
      middleHead = temp2

    return 

if __name__ == "__main__":
  values = [z for z in range(10)]
  solution = Solution()
  listOps = ListOperations()
  #Create and display sample linked list.
  head = listOps.create(values)
  listOps.disp(head)
  #Reorder:
  solution.reorderList(head)
  #Display reordered list.
  listOps.disp(head)
#Reverse Linked list
#Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    def reverseList(self, head):
      prev, curr = None, head
      while curr:
        temp = curr.next #Save original next node
        curr.next = prev #Reverse node direction
        prev = curr #Advance prev pointer
        curr = temp #Advance curr pointer
      return prev
    
    def printlinkedList(self, head):
      current = head
      values = []
      while current:
        values.append(str(current.val))
        current = current.next
      print(" -> ".join(values))
      
    def create_linkedList(self, values: [list]):
      if not values:
        return None
      head = ListNode(values[0])
      current = head
      for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
      return head
      
if __name__ == "__main__":
  values = [1, 3, 5, 7, 9]
  solution = Solution()
  #Create a sample linked list
  head = solution.create_linkedList(values)
  
  #Print original list:
  print("Original list:")
  solution.printlinkedList(head)
  
  #Reverse list
  head = solution.reverseList(head)
  
  #Print reversed list
  print("Reversed list:")
  solution.printlinkedList(head)
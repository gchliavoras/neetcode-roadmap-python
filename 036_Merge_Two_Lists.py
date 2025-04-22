#Merge Two Sorted Linked Lists
#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
#The new list should be made up of nodes from list1 and list2.
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
      if not list1: #Preliminary checks.
        return list2
      elif not list2:
        return list1
        
      if list1.val <= list2.val:
        head = list1
        list1 = list1.next
      else:
        head = list2
        list2 = list2.next
      
      curr = head
      while list1 and list2:
        if list1.val <= list2.val:
          curr.next = list1
          list1 = list1.next
        else:
          curr.next = list2
          list2 = list2.next
        curr = curr.next
        
      curr.next = list1 if list1 else list2

      return head
     
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
  values1 = [-9, 3]
  values2 = [5, 7]
  solution = Solution()
  #Create two linked lists.
  list1 = solution.create_linkedList(values1)
  list2 = solution.create_linkedList(values2)
  
  #Print original lists:
  print("Original lists:")
  solution.printlinkedList(list1)
  solution.printlinkedList(list2)
  
  #Merge Lists:
  head = solution.mergeTwoLists(list1, list2)

  #Print merged list:
  print("Merged list:")
  solution.printlinkedList(head)
#Copy Linked List with Random Pointer
#You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.
#Create a deep copy of the list.
#The deep copy should consist of exactly n new nodes, each including:
#The original value val of the copied node
#A next pointer to the new node corresponding to the next pointer of the original node
#A random pointer to the new node corresponding to the random pointer of the original node
#Note: None of the pointers in the new list should point to nodes in the original list.
#Return the head of the copied linked list.
#In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
      #Create node copies, interleaved in the original list. First pass: create nodes. ...Original-Copy-Original-...
      if not head:
        return None
      current = head
      while current:
        temp = current.next
        current.next = Node(current.val)
        current = current.next
        current.next = temp
        current = current.next
      #Second pass: add random pointers.
      current = head
      while current:
        random = current.random #Original random pointer.
        current = current.next #Move to copied node.
        current.random = random.next if random else None #Link to copy of original random pointer.
        current = current.next #Move to next original node.
      #De-interleave the original list from the copy.
      head_copy = head.next
      current = head
      current_copy = head_copy
      while current:
        current.next = current.next.next
        current = current.next
        current_copy.next = current.next if current else None
        current_copy = current_copy.next
      
      return head_copy

def build_linked_list(data):
    if not data:
        return None

    # Step 1: Create all nodes without setting next/random
    nodes = [Node(val) for val, _ in data]

    # Step 2: Set next and random pointers
    for i, (val, rand_index) in enumerate(data):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if rand_index is not None:
            nodes[i].random = nodes[rand_index]

    return nodes[0]  # Return head of the linked list

def print_linked_list(head):
    nodes = []
    index_map = {}  # Map from Node to its index
    current = head
    index = 0
    while current:
        index_map[current] = index
        nodes.append(current)
        current = current.next
        index += 1

    result = []
    for node in nodes:
        rand_idx = index_map[node.random] if node.random else None
        result.append([node.val, rand_idx])
    print(result)

def is_deep_copy(original, copy):
    orig_nodes = []
    copy_nodes = []
    o, c = original, copy
    while o and c:
        if o is c:
            return False  # They should not be the same objects
        if o.val != c.val:
            return False
        orig_nodes.append(o)
        copy_nodes.append(c)
        o = o.next
        c = c.next

    if o or c:
        return False  # Length mismatch

    # Check random pointers
    orig_index = {node: i for i, node in enumerate(orig_nodes)}
    copy_index = {node: i for i, node in enumerate(copy_nodes)}

    for o_node, c_node in zip(orig_nodes, copy_nodes):
        if o_node.random is None:
            if c_node.random is not None:
                return False
        else:
            o_rand_idx = orig_index[o_node.random]
            c_rand_idx = copy_index.get(c_node.random, -1)
            if o_rand_idx != c_rand_idx:
                return False

    return True

data = [[7, 0], [13, None], [11, 4], [10, 2], [1, 0]]
original = build_linked_list(data)

sol = Solution()
copy = sol.copyRandomList(original)

print("Original:")
print_linked_list(original)

print("Copy:")
print_linked_list(copy)

print("Deep copy check:", is_deep_copy(original, copy))


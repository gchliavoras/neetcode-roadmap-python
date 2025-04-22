#LRU Cache
#Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations
#LRUCache(int capacity) Initialize the LRU cache of size capacity.
#int get(int key) Return the value corresponding to the key if the key exists, otherwise return -1.
#void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.
#A key is considered used if a get or a put operation is called on it.
#Ensure that get and put each run in O(1)O(1) average time complexity.

#Doubly linked list nodes:
class listNode:
  def __init__(self, key: int = 0, value: int = 0):
    self.key = key
    self.val = value
    self.prev = None
    self.next = None

class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = {}
    
    self.head = listNode() 
    self.tail = listNode()
    
    self.head.next = self.tail
    self.tail.prev = self.head
  
  def move_to_end(self, current: 'Optional: listNode') -> None:
    #Check if already at tail of the list.
    if current.next == self.tail:
      return
    #Remove node from current position.
    current.prev.next = current.next
    current.next.prev = current.prev
    #Move before tail of list.
    self.tail.prev.next = current
    current.prev = self.tail.prev
    #Update tail pointer.
    current.next = self.tail
    self.tail.prev = current
    
  def get(self, key: int) -> int:
    if key in self.cache:
      value = self.cache[key].val
      #Mark key as recently used.
      self.move_to_end(self.cache[key])
      #Return key value
      return value

    return -1

  def put(self, key: int, value: int) -> None:
    #Move key to end if already in cache.
    if key in self.cache:
      self.cache[key].val = value
      self.move_to_end(self.cache[key])
    else:
      #Create node and update cache.
      current = listNode(key, value)
      self.cache[key] = current
      #Link node to the tail of the list.
      self.tail.prev.next = current
      current.prev = self.tail.prev
      self.tail.prev = current
      current.next = self.tail
      #If capacity is surpassed, remove the first element of the list and update cache.
      if len(self.cache) > self.capacity:
        LRUNode = self.head.next
        del self.cache[LRUNode.key]
        
        self.head.next = LRUNode.next
        LRUNode.next.prev = self.head

if __name__ == "__main__":
  print("Wecome to the LRUCache creation wizard!")
  capacity = int(input("Enter desired cache capacity:"))
  cache = LRUCache(capacity)
  
  while True:
    choice = input("Input 1 to read from cache, 2 to input a new key-value pair, and 3 to exit.")
    if choice == "1":
      key = input("Input desired key to lookup: ")
      value = cache.get(key)
      if value == -1:
        print("Requested key not in cache.")
      else:
        print(f"Value: {value}")
    elif choice == "2":
      key = input("Input key: ")
      value = input("Input value: ")
      cache.put(key, value)
      print("Key-value pair successfully added to cache!")
    elif choice == "3":
      break
    else:
      print("Invalid input.")

  print("Goodbye!")
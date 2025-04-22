class TimeMap:
#Implement a time-based key-value data structure that supports:
#Storing multiple values for the same key at specified time stamps
#Retrieving the key's value at a specified timestamp
#Implement the TimeMap class:
#TimeMap() Initializes the object.
#void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
#String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".
#Note: For all calls to set, the timestamps are in strictly increasing order.
  def __init__(self):
    self.store = {}

  def set(self, key: str, value: str, timestamp: int) -> None:
    if key not in self.store:
      self.store[key] = []
    self.store[key].append([value, timestamp])

  def get(self, key: str, timestamp: int) -> str:
    result = ""
    valuePairs = self.store.get(key, []) #[value, timestamp] pairs
    #Binary Search in values
    left, right = 0, len(valuePairs) - 1
    while left <= right:
      mid = (left + right) // 2
      if valuePairs[mid][1] == timestamp:
        return valuePairs[mid][0]
        
      elif valuePairs[mid][1] < timestamp:
        result = valuePairs[mid][0]
        left = mid + 1
        
      else:
        right = mid - 1
    
    return result
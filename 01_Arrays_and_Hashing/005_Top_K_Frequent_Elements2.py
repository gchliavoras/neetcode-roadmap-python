import random
class Solution:
  def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    itemFreq = {}
    for num in nums:
      itemFreq[num] = itemFreq.get(num, 0) + 1
      
    freqList = [[] for _ in range(len(nums) + 1)]
    for num, count in itemFreq.items():
      freqList[count].append(num)
      
    Output = []
    for i in range(len(nums), 0, -1):
      for num in freqList[i]:
        Output.append(num)
        if len(Output) == k:
          return Output
  
  def generateRandomList(self, size: int, lower_bound: int, upper_bound: int):
    """
    Generate a list of random integers.
    
    :param size: Number of integers in the list
    :param lower_bound: Minimum possible value of an integer
    :param upper_bound: Maximum possible value of an integer
    :return: List of random integers
    """
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]
  
  def getUserInput(self) -> tuple[int, list[int]]:
    while True:
      try:
        k = int(input("Input k."))
        size = int(input("Input size of test array."))
        return k, size
      except ValueError:
        print("Input must be an integer.")

lower_bound = 1  # Minimum value
upper_bound = 100  # Maximum value

if __name__ == "__main__":
  solution = Solution()
  k, size = solution.getUserInput()
  Input = solution.generateRandomList(size, lower_bound, upper_bound)
  print(solution.topKFrequent(Input, k))
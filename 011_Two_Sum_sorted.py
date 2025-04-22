class Solution:
#Given an array of integers numbers that is sorted in non-decreasing order.
#Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
#There will always be exactly one valid solution.
#Your solution must use O(1) additional space.
  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
      twoSum = numbers[left] + numbers[right]
      if twoSum == target:
        return [left + 1, right + 1]
      elif twoSum > target:
        right += -1
      else:
        left += 1
    raise ValueError(f"No two elements in the input array: {numbers} add up to {target}.")

test_input = [n for n in range(1,11)]
print(test_input)
while True:
  try:
    target = int(input("Enter target:"))
    break
  except ValueError:
    print("Please input a number.")
    
if __name__ == "__main__":
  solution = Solution()
  print(solution.twoSum(test_input, target))
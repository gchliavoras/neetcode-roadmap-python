class Solution:
#There are n cars traveling to the same destination on a one-lane highway.
#You are given two arrays of integers position and speed, both of length n.
#position[i] is the position of the ith car (in miles)
#speed[i] is the speed of the ith car (in miles per hour)
#The destination is at position target miles.
#A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.
#A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.
#If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.
#Return the number of different car fleets that will arrive at the destination
  def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
    res = len(position)
    
    def ETA(pair: list[int]) -> float: #Pair: (Position, speed)
      return (target - pair[0]) / pair[1]
      
    pair_stack = sorted(zip(position, speed)) 
    
    while pair_stack:
      lead_ETA = ETA(pair_stack.pop())
      
      while pair_stack and ETA(pair_stack[-1]) <= lead_ETA:
        pair_stack.pop()
        res -= 1
      
    return res
    
position = [4,1,0,7]
speed = [2,2,1,1]
target = 10
if __name__ == "__main__":
  solution = Solution()
  print(solution.carFleet(target, position, speed))

  
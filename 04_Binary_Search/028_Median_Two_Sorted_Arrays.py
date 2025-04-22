#You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.
#Your solution must run in O(log(m+n)) time.
class Solution:
  def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    
    if len(nums1) <= len(nums2):
      A, B = nums1, nums2
    else:
      A, B = nums2, nums1
      
    m, n = len(A), len(B)
    half_elements = (m + n) // 2 
    
    left, right = 0, m - 1
    while left <= right + 1:
      i = (left + right) // 2 #Index of last element of A before the median of combined A and B.
      j = half_elements - i - 2 #Index of last element of B before the median of combined A and B. -2 because of 0-index
      #For the current mid point, the elements right and left of the mid point for each array. If end of array reached, infinities ensure a comparison is still possible.
      Aleft = A[i] if i >= 0 else float("-inf")
      Bleft = B[j] if j >= 0 else float("-inf")
      Aright = A[i + 1] if i + 1 < m else float("inf")
      Bright = B[j + 1] if j + 1 < n else float("inf")
      #Check if the endpoints i and j are correct.
      if Aleft <= Bright and Bleft <= Aright:
        #Endpoints are correct.
        if (m + n) % 2 != 0:
          #If combined array has odd number of elements, return the middle element.
          return min(Aright, Bright)
        else:
          #Return the average of the middle two elements.
          return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
      
      elif Aleft > Bright:
        #The cutoff index for A was too big.
        right = i - 1
        
      else:
        #The cutoff index for A was too small
        left = i + 1

nums1=[1,2]
nums2=[3]

if __name__ == "__main__":
  solution = Solution()
  print(solution.findMedianSortedArrays(nums1, nums2))
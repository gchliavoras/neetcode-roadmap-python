class Solution:
#Encode and Decode Strings
#Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

  def encode(self, strs: list[str]) -> str:
    length_index: list = []
    joined_string: list = []
    for string in strs:
      length_index.append(str(len(string)))
      joined_string.append(string)
    encoded = ";".join(length_index) + "#" + "".join(joined_string)
    print(f"Encoded: {encoded}")
    return encoded
    
  def decode(self, s: str) -> list[str]:
    index = s.index("#")
    length_index = [int(item) for item in s[:index].split(";") if item]
    joined_string = s[index+1:]
    decoded: list = []
    index_a = 0
    for word_length in length_index:
      index_b = index_a + word_length 
      decoded.append(joined_string[index_a:index_b])
      index_a = index_b
    print(f"Decoded: {decoded}")  
    return decoded

if __name__ == "__main__":
  solution = Solution()
  solution.decode(solution.encode([]))


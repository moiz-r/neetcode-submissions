class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        res = 0
        l = 0
        for r in range(len(s)):
          chars[s[r]] = 1 + chars.get(s[r], 0) # increment freq of letters in window as you encounter them

         # while len of window - most freq letter > k 
         # keep reducing size of window, until it is valid
         # window is valid when len of window - most freq char > k
          while (r - l + 1) - max(chars.values()) > k:
            chars[s[l]] -= 1
            l += 1
          res = max((r - l + 1), res)
        return res
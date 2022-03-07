class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0)
            while (right-left + 1) - max(count.values()) > k:
                count[s[left]] -=1
                left +=1
            max_len = max(max_len, right - left + 1 )
        return max_len
            
        
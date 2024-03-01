class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s):
            return s == s[::-1]
        longest = s[0]
        for l in range(len(s)):
            for r in range(len(s),0,-1):
                if l == r or l > r or len(longest) > r-l+1:
                    continue
                x = s[l:r]
                if is_palindrome(x):
                    if len(x) > len(longest):
                        longest = x
        return longest
                
                
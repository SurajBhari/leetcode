class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)[::-1]
        is_minus = '-' in s
        s = s.replace("-", '')
        s = int(s)
        
        if s > 2147483647:
            return 0
        if is_minus:
            s = s * -1
        return s 
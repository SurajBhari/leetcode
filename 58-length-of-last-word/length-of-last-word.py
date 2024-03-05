class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [x for x in s.split(" ") if x]
        return len(words[-1])
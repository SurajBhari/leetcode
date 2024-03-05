class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len([x for x in s.split(" ") if x][-1])
        
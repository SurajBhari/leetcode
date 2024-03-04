class Solution:
    def repeatedCharacter(self, s: str) -> str:
        known = []
        for c in s:
            if c in known:
                return c
            known.append(c)
        
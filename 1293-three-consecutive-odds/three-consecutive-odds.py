class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        score = 0
        for num in arr:
            if num%2==1:
                score += 1
            else:
                score = 0
            if score >= 3:
                return True

        return False
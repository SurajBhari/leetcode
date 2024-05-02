class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        answers = []
        for x in nums:
            if x*-1 in nums:
                answers.append(x)
                answers.append(x*-1)
        if not answers:
            return -1
        return max(answers)
                
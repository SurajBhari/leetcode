class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for n in list(set(nums1)):
            if n in nums2:
                c1 = nums1.count(n)
                c2 = nums2.count(n)
                answer.extend([n for i in range(min([c1,c2]))])
        return answer
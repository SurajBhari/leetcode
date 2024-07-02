class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [x for x in list(set(nums1)) if x in nums2]
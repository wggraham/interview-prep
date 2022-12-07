class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = set(nums)
        return len(nums) != len(n)
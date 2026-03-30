class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for x in range(len(nums)):
            prod = 1
            for y in range(len(nums)):
                if x == y:
                    continue
                prod *= nums[y]
            res.append(prod)
        return res
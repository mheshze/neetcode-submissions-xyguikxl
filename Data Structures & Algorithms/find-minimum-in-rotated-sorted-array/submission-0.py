class Solution:
    def findMin(self, nums: List[int]) -> int:
        # this is mainly a traversal algo
        l,r = 0, len(nums) - 1
        res = nums[l]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l],res)
                break

            mid = l + (r-l) // 2
            res = min(res,nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        #    0,1,2,3,4,5
        #    5,0,1,2,3,4
        #    4,5,0,1,2,3
        #    3,4,5,0,1,2
        #    2,3,4,5,0,1
        #    1,2,3,4,5,0
        return res
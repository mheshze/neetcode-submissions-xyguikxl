class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hmap = {}
        # for i in range(len(nums)):
        #     rem = target - nums[i]
        #     if rem in hmap:
        #         return [hmap[rem], i ]
        #     hmap[nums[i]] = i

        ''' do this in with two pointers '''
        arr = []
        for i,val in enumerate(nums):
            arr.append([val,i])
        arr.sort()
        
        l,r = 0, len(arr) - 1
        while l < r:
            twosum = arr[l][0] + arr[r][0]
            if twosum > target:
                r -= 1
            elif twosum < target:
                l += 1
            else:
                return [min(arr[l][1],arr[r][1]), max(arr[l][1],arr[r][1])]






            
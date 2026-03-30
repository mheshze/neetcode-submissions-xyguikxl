class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        #  test cases
            # 1,2,3,4,5,6
            # 6,1,2,3,4,5
            # 5,6,1,2,3,4
            # 4,5,6,1,2,3 
            # 3,4,5,6,1,2
            # 2,3,4,5,6,1
        
        # single pass
        while l <= r:
            mid = l + (r-l) // 2
            if target == nums[mid]:
                return mid            

            # left half is sorted
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
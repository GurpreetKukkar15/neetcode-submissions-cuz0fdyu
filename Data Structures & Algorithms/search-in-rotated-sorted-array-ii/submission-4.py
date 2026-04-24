class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r= 0, len(nums)-1
        while l <= r:
            mid= (l+r)//2
            if nums[mid]==target:
                return True
            elif nums[l] == nums[r]:
                if nums[l] == target:
                    return True
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if target < nums[l]:
                    l= mid + 1
                elif target < nums[mid]:
                    r= mid - 1
                else:
                    l= mid + 1

            else:  # right half sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
            
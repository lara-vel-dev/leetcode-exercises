'''
-- 35. Search Insert Position --
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

Examples:
Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Constraints:
* 1 <= nums.length <= 104
* -104 <= nums[i] <= 104
* nums contains distinct values sorted in ascending order.
* -104 <= target <= 104
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums.sort()

        return nums.index(target)


sol = Solution()
print(sol.searchInsert([1, 3, 5, 6], 5))

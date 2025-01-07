from typing import List

'''
-- 1480. Running Sum of 1d Array --

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Constraints:
* 1 <= nums.length <= 1000
* -10^6 <= nums[i] <= 10^6
'''


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        self.new_array = []
        self.counter = 0
        for num in nums:
            self.counter += num
            self.new_array.append(self.counter)

        return self.new_array

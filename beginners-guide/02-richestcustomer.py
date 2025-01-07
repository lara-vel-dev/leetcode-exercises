'''
-- 1672. Richest Customer Wealth --

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.

Example:
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.

Constraints:
* m == accounts.length
* n == accounts[i].length
* 1 <= m, n <= 50
* 1 <= accounts[i][j] <= 100
'''


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        self.max_value = 0
        for account in accounts:
            self.counter = 0
            for num in account:
                self.counter += num
            self.max_value = max(self.max_value, self.counter)

        return self.max_value

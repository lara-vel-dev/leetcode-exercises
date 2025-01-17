'''
-- 1408. String Matching in an Array --

Given an array of string words, return all strings in words that is a substring of another word. 
You can return the answer in any order.
A substring is a contiguous sequence of characters within a string

Examples:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.

Constraints:
* 1 <= words.length <= 100
* 1 <= words[i].length <= 30
* words[i] contains only lowercase English letters.
* All the strings of words are unique.
'''


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        self.arr = []
        for word in words:
            for i in range(len(words)):
                if word in words[i] and words[i] != word:
                    self.arr.append(word)
                    break

        return self.arr

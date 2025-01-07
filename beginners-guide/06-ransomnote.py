'''
-- 383. Ransom Note --

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine.
Rreturn false otherwise.
Each letter in magazine can only be used once in ransomNote.

Examples:
Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
* 1 <= ransomNote.length, magazine.length <= 105
* ransomNote and magazine consist of lowercase English letters.
'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i not in magazine:
                return False
            magazine = magazine.replace(i, "", 1)
        return True

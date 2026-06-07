class Solution:
    def validPalindrome(self, s: str) -> bool:
        res = False
        for i in range(len(s)):
            newStr = s
            newStr = newStr[:i] + newStr[i + 1:]
            if self.isPalindrome(newStr):
                res = True
        return res

    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

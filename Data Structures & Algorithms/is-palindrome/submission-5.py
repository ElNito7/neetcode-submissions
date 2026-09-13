class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep alphanumerical characteres and remove the rest
        text = "".join(char for char in s if char.isalnum()).lower()

        if not text:
            return True

        # Two Pointers
        left = 0 # start
        right = len(text) - 1 # end
        mid = len(text) / 2

        while left != right and left <= mid: 
            if text[left] != text[right]:
                return False
            left += 1
            right -= 1
        
        return True
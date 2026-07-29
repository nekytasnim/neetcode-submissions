class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = re.sub(r'[^a-zA-Z0-9/s]', '', s)
        s_lower = s_cleaned.lower()
        front = 0
        end = len(s_lower) - 1

        while front < end:
            if s_lower[front] != s_lower[end]:
                return False
            front += 1
            end -= 1
        return True
            

        
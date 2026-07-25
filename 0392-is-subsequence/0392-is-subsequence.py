class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Use two pointer approach
        pointer_s = 0
        pointer_t = 0
        try:
            while True:
                if s[pointer_s] == t[pointer_t]:
                    s = s[1:]
                    pointer_t += 1
                else:
                    pointer_t += 1
        except:
            if len(s) == 0:
                return True
            else:
                return False
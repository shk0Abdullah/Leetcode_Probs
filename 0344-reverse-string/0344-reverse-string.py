class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        frwd_pointer = 0
        end_pointer = len(s)-1
        while True:
            if end_pointer > frwd_pointer:
                s[frwd_pointer],s[end_pointer] = s[end_pointer],s[frwd_pointer]
                end_pointer -= 1
                frwd_pointer += 1
            else:
                break
        return s

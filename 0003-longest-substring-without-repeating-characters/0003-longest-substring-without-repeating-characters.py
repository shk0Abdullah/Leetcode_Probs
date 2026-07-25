class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev_ctx = ""
        curr_ctx = ""
        # Use Sliding window
        # if you find any character repeating in the context skip it and add the rest of it
        # make the context reset when you want to make it a new 


        for ch in s:

            if ch not in curr_ctx:
                curr_ctx += ch

            else:
                # Save best window so far
                if len(curr_ctx) > len(prev_ctx):
                    prev_ctx = curr_ctx

                # Find duplicate in CURRENT window
                idx = curr_ctx.index(ch)

                # Keep everything after duplicate
                curr_ctx = curr_ctx[idx + 1:] + ch

        # Compare the last window
        if len(curr_ctx) > len(prev_ctx):
            prev_ctx = curr_ctx

        return len(prev_ctx)

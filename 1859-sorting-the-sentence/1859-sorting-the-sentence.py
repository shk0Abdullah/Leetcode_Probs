class Solution:
    def sortSentence(self, s: str) -> str:
        ls = s.split()
        sorted_ls = [None] * len(ls)
        for i in ls:
            index = int(i[-1]) - 1
            sorted_ls[index] = i[:-1]
        return(" ".join(sorted_ls))

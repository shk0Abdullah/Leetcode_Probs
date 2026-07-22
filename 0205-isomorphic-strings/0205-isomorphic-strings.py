class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        if len(s) == len(t):
            for i in range(len(s)):
                if t[i] in dic.values() and dic.get(s[i]) != t[i]:

                    return False
                else:
                    if dic.get(s[i]) and dic.get(s[i]) != t[i]:
                        return False
                    dic[s[i]] = t[i]
                    print(dic.get(s[i]), t[i])
            return True
                 
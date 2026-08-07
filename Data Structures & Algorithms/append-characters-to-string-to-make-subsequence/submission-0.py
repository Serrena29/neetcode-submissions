class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        cnt = 0
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i]==t[j]:
                i += 1
                j += 1
            else:
                i += 1
        for k in range(j, len(t)):
            cnt += 1

        return cnt           
class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        for i in range(0, len(s)-1, 2):
            x,y = s[i], s[i+1]
            if x != y:
                count += 1
        return count
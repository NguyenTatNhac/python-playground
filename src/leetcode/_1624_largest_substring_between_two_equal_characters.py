class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_index = {}
        result = -1
        for i in range(len(s)):
            if s[i] in first_index:
                result = max(result, i - first_index[s[i]] - 1)
            else:
                first_index[s[i]] = i
        return result

tmp = Solution()
res = tmp.maxLengthBetweenEqualCharacters("abvbar")
print(res)
import collections


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        countMap = collections.defaultdict(list)
        for i in range(len(s)):
            countMap[s[i]].append(i)

        result = -1
        for count in countMap:
            position_arr = countMap[count]
            if len(position_arr) > 1:
                result = max(result, position_arr[-1] - position_arr[0] - 1)
        return result

tmp = Solution()
res = tmp.maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv")
print(res)
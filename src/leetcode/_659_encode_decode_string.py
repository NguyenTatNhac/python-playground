class Solution:
    def encode(self, strs):
        res = ''
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, str):
        res, i = [], 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            l = int(str[i:j])
            res.append(str[j + 1:j + 1 + l])
            i = j + 1 + l

        return res
    
tmp = Solution()
encoded = tmp.encode(["Hello", "I", "am", "a", "Good Boy", "##43#"])
print(encoded)
decoded = tmp.decode(encoded)
print(decoded)

    
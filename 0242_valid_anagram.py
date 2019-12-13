class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for l in s:
            if l not in t:
                return False
            t = t.replace(l, '', 1)
        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    solution = Solution()
    result = solution.isAnagram('aaca', 'ccac')
    print(result)
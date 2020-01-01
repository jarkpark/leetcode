class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # s_ct = {}
        # t_ct = {}
        # s_map = []
        # t_map = []
        # for letter in s:
        #     if letter not in s_ct:
        #         s_ct[letter] = len(s_ct)
        #         s_map.append(s_ct[letter])
        #     else:
        #         s_map.append(s_ct[letter])
        # for letter in t:
        #     if letter not in t_ct:
        #         t_ct[letter] = len(t_ct)
        #         t_map.append(t_ct[letter])
        #     else:
        #         t_map.append(t_ct[letter])
        # if s_map == t_map:
        #     return True
        # else:
        #     return False

        lmap = {}
        i = 0
        for letter in s:
            if letter not in lmap:
                lmap[letter] = str(i)
                i += 1
        for k, v in lmap.items():
            s = s.replace(k, v)

        lmap.clear()
        i = 0
        for letter in t:
            if letter not in lmap:
                lmap[letter] = str(i)
                i += 1
        for k, v in lmap.items():
            t = t.replace(k, v)

        if s == t:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    result = solution.isIsomorphic('egg', 'add')
    print(result)
    result = solution.isIsomorphic('foo', 'bar')
    print(result)

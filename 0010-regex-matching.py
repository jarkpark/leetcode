class Solution(object):
    def isMatch(self, s, p):
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])


if __name__ == '__main__':
    sol = Solution()
    inputs = [
        ('aa', 'a'),
        ('aa', 'a*'),
        ('ab', '.*'),
        ('aab', 'c*a*b'),
        ('mississippi', 'mis*is*p*.'),
        ('ab', '.*c'),
        ('aaa', 'aaaa'),
        ('aaa', 'a*a')
    ]
    for input in inputs:
        print(sol.isMatch(*input))

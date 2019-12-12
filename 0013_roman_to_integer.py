class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        one_offs = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        result = 0
        for one_off in one_offs:
            count = s.count(one_off)
            if count:
                result += count * mapping[one_off]
                s = s.replace(one_off, '')
        for l in s:
            result += mapping[l]
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.romanToInt('MCMXCIV')
    print(result)

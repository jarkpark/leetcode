class Solution:
    def reverseWords(self, s: str) -> str:
        s_arr = s.split()
        for i in range(len(s_arr)):
            s_arr[i] = s_arr[i][::-1]
        result = ' '.join(s_arr)
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.reverseWords("Let's take LeetCode contest")
    print(result)
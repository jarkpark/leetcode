from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        unique_transforms = set()
        for word in words:
            transform = ''
            for l in word:
                transform += morse[alpha.index(l)]
            unique_transforms.add(transform)
        return len(unique_transforms)


if __name__ == '__main__':
    solution = Solution()
    result = solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
    print(result)

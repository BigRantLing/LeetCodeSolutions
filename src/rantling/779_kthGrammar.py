# coding= utf-8


class Solution(object):
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0

        father = self.kthGrammar(N-1, (K+1) // 2)

        if father == 0:
            return 0 if K % 2 == 1 else 1
        if father == 1:
            return 0 if K % 2 == 0 else 1


if __name__ == '__main__':
    res = Solution().kthGrammar(30, 434991989)
    print(res)

class Solution:
    def kClosest(self, points, K):
        comparator = lambda point: point[0]**2 + point[1]**2
        points.sort(key=comparator)
        return points[:K]

if __name__ == '__main__':
    solution = Solution()
    print(solution.kClosest([[1, 1], [2, 3], [4, 7]], 2))
    print(solution.kClosest([[1, 0], [0, 1]], 2))
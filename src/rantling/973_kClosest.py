class Solution:
    def kClosest(self, points, K):
        self.points = points
        pointsLength = len(points)

        if pointsLength <= K:
            return points

        for i in range(0, pointsLength-1):
            currDistance = self.distance(points[i])
            for j in range(i+1, pointsLength):
                nextDistance = self.distance(points[j])
                if nextDistance <= currDistance:
                    self.exchange(i, j)

            # if i+1 == K:
            #     return points[:K]
        return points

    def distance(self, point):
        return point[0]**2 + point[1]**2

    def exchange(self, leftIndex, rightIndex):
        tmp = self.points[leftIndex]
        self.points[leftIndex] = self.points[rightIndex]
        self.points[rightIndex] = tmp



if __name__ == '__main__':
    solution = Solution()
 #   print(solution.kClosest([[1, 1], [2, 3], [4, 7]], 2))
    print(solution.kClosest([[68,97],[34,-84],[60,100],[2,31],[-27,-38],[-73,-74],[-55,-39],[62,91],[62,92],[-57,-67]], 5))
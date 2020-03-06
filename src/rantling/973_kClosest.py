class Solution:
    def kClosest(self, points, K):
        self.points = points
        pointsLength = len(points)

        if pointsLength <= K:
            return points

        distance = lambda point: point[0]**2 + point[1]**2

        for i in range(0, pointsLength-1):
            for j in range(0, pointsLength-1-i):
                if distance(points[j]) < distance(points[j+1]):
                    self.exchange(j, j+1)

            if i+1 == K:
                return points[-5:]
        return points

    def exchange(self, leftIndex, rightIndex):
        tmp = self.points[leftIndex]
        self.points[leftIndex] = self.points[rightIndex]
        self.points[rightIndex] = tmp


if __name__ == '__main__':
    solution = Solution()
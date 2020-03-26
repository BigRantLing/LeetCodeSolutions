class Solution:
    def surfaceArea(self, grid) -> int:
        self.marker = []
        self.N = len(grid)
        for row in range(0,  self.N):
            self.marker.append([False]*self.N)
               
        self.grid = grid
        total_area = 0

        for row in range(0, self.N):
            for col in range(0, self.N):
                total_area += self.__dfs(row, col)

        return total_area

    def __dfs(self, row, col):

        if self.marker[row][col] is True or self.grid[row][col] == 0:
            return 0

        self.marker[row][col] = True
        cube_ammount = self.grid[row][col]
        area = cube_ammount*6-2*(cube_ammount-1)

        nebs = self.__getAdj(row, col)
        for neb in nebs:
            neb_ammount = self.grid[neb[0]][neb[1]]
            area -= cube_ammount if cube_ammount <= neb_ammount else neb_ammount

        print("%d area %d" % (cube_ammount, area))

        for neb in nebs:
            area += self.__dfs(neb[0], neb[1])

        return area

    def __getAdj(self, row, col):
        nebs = []
        # up
        if row - 1 >= 0:
            nebs.append([row - 1, col])
        # down
        if row + 1 < self.N:
            nebs.append([row + 1, col])
        # left
        if col - 1 >= 0:
            nebs.append([row, col - 1])
        # right
        if col + 1 < self.N:
            nebs.append([row, col + 1])

        return nebs


if __name__ == '__main__':
    print(Solution().surfaceArea([[1,0],[0,2]]))
# coding: utf-8


class Solution:
    def solve(self, board):
        if len(board) == 0:
            return

        self.board_higth = len(board)
        self.board_with = len(board[0])
        self.board = board

        # 遍历第一行和最后一行
        for row in (0, self.board_higth-1):
            for col in range(0, self.board_with):
                if board[row][col] == 'O':
                    self.__dfs(row, col)

        # 遍历第一列和最后一列
        for col in (0, self.board_with-1):
            for row in range(0, self.board_higth):
                if self.board[row][col] == 'O':
                    self.__dfs(row, col)

        for row in range(0, self.board_higth):
            for col in range(0, self.board_with):
                if self.board[row][col] == '#':
                    print('O', end='    ')
                else:
                    print('X', end='    ')

            print('\n')

    def __dfs(self, row: int, col: int):
        # 标记所有连通的'O'
        if self.board[row][col] != '#':
            self.board[row][col] = '#'

            for point in self.__getAdjacency(row, col):
                self.__dfs(point[0], point[1])

    # 返回所有为'O'的邻接位置
    def __getAdjacency(self, row: int, col: int):
        adjacency_list = []

        if row - 1 > 0 and self.board[row-1][col] == 'O':
            adjacency_list.append((row - 1, col))

        if row + 1 < self.board_higth and self.board[row+1][col] == 'O':
            adjacency_list.append((row + 1, col))

        if col - 1 > 0 and self.board[row][col-1] == 'O':
            adjacency_list.append((row, col - 1))

        if col + 1 < self.board_with and self.board[row][col+1] == 'O':
            adjacency_list.append((row, col + 1))

        return adjacency_list


if __name__ == '__main__':
    Solution().solve([["X", "O", "X", "O", "X", "O"],
                      ["O", "X", "O", "X", "O", "X"],
                      ["X", "O", "X", "O", "X", "O"],
                      ["O", "X", "O", "X", "O", "X"]])

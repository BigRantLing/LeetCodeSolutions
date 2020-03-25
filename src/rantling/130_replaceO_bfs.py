# coding: utf-8
import queue


class Solution:
    def solve(self, board):        
        if len(board) == 0:
            return

        self.queue = queue.Queue(0)
        self.board = board
        self.board_width = len(board[0])
        self.board_higth = len(board)

        # 遍历第一行和最后一行
        for row in (0, self.board_higth-1):
            for col in range(0, self.board_width):
                if self.board[row][col] == 'O':
                    self.queue.put((row, col))
                    while self.queue.qsize() > 0:
                        point = self.queue.get(False)
                        self.__bfs(point[0], point[1])

        # 遍历第一列和最后一列
        for col in (0, self.board_width-1):
            for row in range(0, self.board_higth):
                if self.board[row][col] == 'O':
                    self.queue.put((row, col))
                    while self.queue.qsize() > 0:
                        point = self.queue.get(False)
                        self.__bfs(point[0], point[1])

        for row in range(0, self.board_higth):
            for col in range(0, self.board_width):
                if self.board[row][col] == '#':
                    self.board[row][col] = 'O'
                    print('O', end='    ')
                else:
                    self.board[row][col] = 'X'
                    print('X', end='    ')
            print('\n')

    def __bfs(self, row, col):
        if self.board[row][col] != '#':
            self.board[row][col] = '#'
        self.__put_adjacency(row, col)

    def __put_adjacency(self, row, col):
        if row - 1 > 0 and self.board[row-1][col] == 'O':
            self.queue.put((row - 1, col))

        if row + 1 < self.board_higth and self.board[row+1][col] == 'O':
            self.queue.put((row + 1, col))

        if col - 1 > 0 and self.board[row][col-1] == 'O':
            self.queue.put((row, col - 1))

        if col + 1 < self.board_width and self.board[row][col+1] == 'O':
            self.queue.put((row, col + 1))


if __name__ == '__main__':
    Solution().solve([["X", "O", "X", "O", "O", "O"],
                      ["O", "X", "O", "X", "O", "X"],
                      ["X", "O", "X", "O", "O", "O"],
                      ["O", "X", "O", "X", "O", "X"]])

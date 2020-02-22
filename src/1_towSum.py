class Solution:
    def twoSum(self, nums, target):
        currIndex = 0
        length = len(nums)

        for num in nums:
            currIndex += 1
            rest = target - num
            
            for index in range(currIndex, length):
                if rest == nums[index]:
                    return [currIndex-1, index]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([1, 0, 9, 2, 7, 8], 9))

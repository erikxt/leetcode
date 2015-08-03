__author__ = 'erica'


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        index = {}
        for i, num in enumerate(nums, 1):
            print i, num
            try:
                return index[target-num], i
            except:
                index[num] = i


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    s = Solution()
    res = s.twoSum(numbers, target)
    print res

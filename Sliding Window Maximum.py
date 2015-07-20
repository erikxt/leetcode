__author__ = 'erik'


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        if len(nums) == 0:
            return []
        ans, tmp = [], []
        for i in range(0, k):
            while tmp != [] and nums[i] > nums[tmp[-1]]:
                tmp.pop()
                n += 1
            tmp.append(i)
        for i in range(k, len(nums)):
            ans.append(nums[tmp[0]])
            while tmp != [] and nums[i] > nums[tmp[-1]]:
                m += 1
                tmp.pop()
            tmp.append(i)
            while tmp != [] and tmp[0] <= i - k:
                m += 1
                tmp.pop(0)
        ans.append(nums[tmp[0]])
        return ans

if __name__ == '__main__':
    nums = (1, 3, 1, 2, 0, 5)
    k = 3
    s = Solution()
    print s.maxSlidingWindow(nums, k)

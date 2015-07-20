__author__ = 'erik'


class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        if not nums:
            return []
        tmp, res = [0] * 2, [0, 1]
        for i in range(len(nums)):
            if tmp[0] == 0 and nums[i] != res[1]:
                tmp[0] = 1
                res[0] = nums[i]
            elif tmp[1] == 0 and nums[i] != res[0]:
                tmp[1] = 1
                res[1] = nums[i]
            elif nums[i] not in res:
                for j in range(len(res)):
                    tmp[j] -= 1
            elif nums[i] in res:
                tmp[res.index(nums[i])] += 1
        return [n for n in res if nums.count(n) > len(nums) // 3]


if __name__ == '__main__':
    nums = [0] * 3
    s = Solution()
    print s.majorityElement(nums)


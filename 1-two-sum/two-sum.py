class Solution:
    def twoSum(self, nums, target):
        mp = {}   # dictionary to store value:index

        for i in range(len(nums)):
            complement = target - nums[i]

            # check if complement already exists
            if complement in mp:
                return [mp[complement], i]

            # store current element with index
            mp[nums[i]] = i


# Driver Code
nums = [2, 7, 11, 15]
target = 9

sol = Solution()
print(sol.twoSum(nums, target))
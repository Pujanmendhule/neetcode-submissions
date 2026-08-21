class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res ={}

        for i in range(len(nums)):
            wanted = target - nums[i]

            if wanted in res:
                return [res[wanted],i]
            else:
                res[nums[i]]=i
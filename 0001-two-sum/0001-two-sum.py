class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diction = {}

        for index, num in enumerate(nums):

            diff = target - num

            if diff in diction:
                 return [index, diction[diff]]

            diction[num]  = index

        return []



        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictionary = {} # keeps track of the previous values we have already seen

        for index, value in enumerate(nums):
            diff = target - value
            if diff in dictionary:
                return [dictionary[diff], index]
            dictionary[value] = index
        
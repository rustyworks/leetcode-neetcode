class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        number_dictionary: dict[int, int] = {}
        for index, num in enumerate(nums):
            remaining = target - num
            if number_dictionary.get(remaining, None) is not None:
                return [number_dictionary[remaining], index]
            else:
                number_dictionary[num] = index
        return [-1, -1]

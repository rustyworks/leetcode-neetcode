class Solution():
    def containsDuplicate(self, nums: list[int]) -> bool:
        number_map = {}
        for num in nums:
            if num in number_map:
                return True
            else:
                number_map[num] = 1
        return False

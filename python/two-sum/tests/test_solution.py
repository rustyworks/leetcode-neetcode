from two_sum.solution import Solution


def test_correct_two_sum():
    solution = Solution()
    assert [0, 1] == solution.twoSum([2, 7, 11, 15], 9), f"Result {solution.twoSum([2, 7, 11, 15], 9)}"
    assert [1, 2] == solution.twoSum([3, 2, 4], 6)
    assert [0, 1] == solution.twoSum([3, 3], 6)


def test_all():
    test_correct_two_sum()

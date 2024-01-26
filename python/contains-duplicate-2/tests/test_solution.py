from contains_duplicate_2.solution import Solution

def return_true_if_contains_duplicate():
    nums_1 = [1, 2, 3, 1]
    nums_2 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    solution = Solution()
    assert solution.containsDuplicate(nums_1) == True
    assert solution.containsDuplicate(nums_2) == True


def return_false_if_not_contains_duplicate():
    nums = [1, 2, 3, 4]
    solution = Solution()
    assert solution.containsDuplicate(nums) == False


def test_all():
    return_true_if_contains_duplicate()
    return_false_if_not_contains_duplicate()

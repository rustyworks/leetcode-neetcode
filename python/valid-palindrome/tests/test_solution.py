from valid_palindrome.solution import Solution


def test_valid_palindrome():
    solution = Solution()
    assert solution.isPalindrome("A man, a plan, a canal: Panama")


def test_invalid_palindrome():
    solution = Solution()
    assert not solution.isPalindrome("race a car")


def test_spaces_only():
    solution = Solution()
    assert solution.isPalindrome(" ")


def test_with_underscore():
    solution = Solution()
    assert solution.isPalindrome("ab_a")


def test_all():
    test_valid_palindrome()
    test_invalid_palindrome()
    test_spaces_only()
    test_with_underscore()

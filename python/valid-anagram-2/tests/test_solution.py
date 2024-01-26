from valid_anagram_2.solution import Solution


def return_true_if_anagram_valid():
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    assert solution.isAnagram(s, t) == True


def return_false_if_anagram_invalid():
    s = "rat"
    t = "car"
    solution = Solution()
    assert solution.isAnagram(s, t) == False

    s = "a"
    t = "ab"
    solution = Solution()
    assert solution.isAnagram(s, t) == False


def test_all():
    return_true_if_anagram_valid()
    return_false_if_anagram_invalid()

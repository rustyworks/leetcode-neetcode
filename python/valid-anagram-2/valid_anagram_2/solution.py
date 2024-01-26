class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        key_map: dict[str, int] = {}
        for char_1, char_2 in zip(s, t):
            if char_1 in key_map:
                key_map[char_1] += 1
            else:
                key_map[char_1] = 1
            if char_2 in key_map:
                key_map[char_2] -= 1
            else:
                key_map[char_2] = -1
        for v in key_map.values():
            if v != 0:
                return False
        return True

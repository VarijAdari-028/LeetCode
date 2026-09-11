class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        from itertools import permutations

        results = set()

        for perm in permutations(digits, 3):
            if perm[0] != 0 and perm[2] % 2 == 0:
                results.add(perm)

        return len(results)
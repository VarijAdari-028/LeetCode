class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        n = len(nums1)

        def can_all(parity):
            for x in nums1:
                if x % 2 == parity:
                    continue
                found = False
                for y in nums1:
                    if y == x:
                        continue
                    if (x - y) % 2 == parity:
                        found = True
                        break
                if not found:
                    return False
            return True

        return can_all(0) or can_all(1)
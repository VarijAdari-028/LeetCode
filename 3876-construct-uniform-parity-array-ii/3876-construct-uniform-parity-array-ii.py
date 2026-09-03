class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        nums_sorted = sorted(nums1)

        def can_all(parity):
            seen = [False, False]  # seen[0] = seen an even element so far, seen[1] = seen an odd
            for x in nums_sorted:
                if x % 2 != parity:
                    need_parity = (x - parity) % 2
                    if not seen[need_parity]:
                        return False
                seen[x % 2] = True
            return True

        return can_all(0) or can_all(1)
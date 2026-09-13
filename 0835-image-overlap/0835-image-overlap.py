class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
        ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]

        if not ones1 or not ones2:
            return 0

        from collections import defaultdict
        shift_counts = defaultdict(int)

        for x1, y1 in ones1:
            for x2, y2 in ones2:
                shift_counts[(x1 - x2, y1 - y2)] += 1

        return max(shift_counts.values())
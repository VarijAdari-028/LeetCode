class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        left = (1 << 1) | (1 << 2) | (1 << 3) | (1 << 4)    # 2-5
        middle = (1 << 3) | (1 << 4) | (1 << 5) | (1 << 6)  # 4-7
        right = (1 << 5) | (1 << 6) | (1 << 7) | (1 << 8)   # 6-9

        reserved = {}

        for row, seat in reservedSeats:
            reserved[row] = reserved.get(row, 0) | (1 << (seat - 1))
        answer = (n - len(reserved)) * 2

        for mask in reserved.values():

           
            if (mask & left) == 0 and (mask & right) == 0:
                answer += 2

            elif (mask & left) == 0 or (mask & middle) == 0 or (mask & right) == 0:
                answer += 1

        return answer
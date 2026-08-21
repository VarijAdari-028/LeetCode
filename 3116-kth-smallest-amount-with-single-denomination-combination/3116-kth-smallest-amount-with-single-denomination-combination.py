class Solution:
    def findKthSmallest(self, coins, k):
        from math import gcd

        n = len(coins)

        # Calculate LCM of two numbers
        def lcm(a, b):
            return a // gcd(a, b) * b

        # Remove redundant coins.
        # If a coin is a multiple of another coin,
        # it doesn't add any new amounts.
        coins.sort()
        useful = []

        for c in coins:
            if all(c % x != 0 for x in useful):
                useful.append(c)

        coins = useful
        n = len(coins)

        # Precompute LCM for every subset
        subset_lcm = [1] * (1 << n)

        for mask in range(1, 1 << n):
            # Get one set bit
            bit = mask & -mask
            i = bit.bit_length() - 1

            prev = mask ^ bit

            if prev == 0:
                subset_lcm[mask] = coins[i]
            else:
                value = lcm(subset_lcm[prev], coins[i])

                # If LCM is too large, it will never
                # contribute for our relevant x.
                if value > 10**18:
                    value = 10**18

                subset_lcm[mask] = value

        # Count numbers <= x divisible by at least one coin
        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                L = subset_lcm[mask]

                if L > x:
                    continue

                multiples = x // L

                # Odd number of coins -> add
                if mask.bit_count() % 2 == 1:
                    total += multiples
                else:
                    total -= multiples

            return total

        # Binary search
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
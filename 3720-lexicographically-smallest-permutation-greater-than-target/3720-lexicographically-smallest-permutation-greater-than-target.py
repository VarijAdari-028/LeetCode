class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        best_pos = -1
        best_char = -1

        for i in range(len(target)):
            x = ord(target[i]) - ord('a')

            # Find the smallest character greater than target[i]
            for c in range(x + 1, 26):
                if count[c] > 0:
                    best_pos = i
                    best_char = c
                    break

            # Keep matching target if possible
            if count[x] == 0:
                break

            count[x] -= 1

        if best_pos == -1:
            return ""

        # Rebuild counts
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Use target's prefix
        for i in range(best_pos):
            count[ord(target[i]) - ord('a')] -= 1

        # Use the character that makes it greater
        count[best_char] -= 1

        # Add remaining characters in sorted order
        ans = target[:best_pos] + chr(best_char + ord('a'))

        for c in range(26):
            ans += chr(c + ord('a')) * count[c]

        return ans
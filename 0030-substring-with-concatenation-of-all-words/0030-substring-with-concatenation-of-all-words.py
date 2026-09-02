class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        n = len(s)

        if total_len > n:
            return []

        word_count = {}
        for w in words:
            word_count[w] = word_count.get(w, 0) + 1

        result = []

        # sliding window per starting offset (0..word_len-1)
        for offset in range(word_len):
            left = offset
            count = 0
            window_count = {}

            for right in range(offset, n - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_count:
                    window_count[word] = window_count.get(word, 0) + 1
                    count += 1

                    # if this word now exceeds what's needed, shrink from the left
                    while window_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        window_count[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == num_words:
                        result.append(left)
                        # slide window forward by one word to look for next match
                        left_word = s[left:left + word_len]
                        window_count[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    # word not in words at all: reset window past this point
                    window_count.clear()
                    count = 0
                    left = right + word_len

        return result
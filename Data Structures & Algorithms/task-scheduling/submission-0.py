class Solution:
    def leastInterval(self, tasks, n):

        from collections import Counter

        freq = Counter(tasks)

        max_freq = max(freq.values())

        count_max = 0
        for f in freq.values():
            if f == max_freq:
                count_max += 1

        ans = (max_freq - 1) * (n + 1) + count_max

        return max(len(tasks), ans)




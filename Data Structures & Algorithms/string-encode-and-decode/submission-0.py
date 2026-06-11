from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # Find the separator '#'
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            # Extract the string of given length
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            # Move to the next encoded string
            i = j + 1 + length

        return res
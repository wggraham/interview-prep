from typing import List
from collections import defaultdict
from sys import maxsize


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        maxAttack = -maxsize
        minAttack = maxsize

        maxDefense = defaultdict(int)
        for attack, defense in properties:
            maxDefense[attack] = max(maxDefense[attack], defense)
            maxAttack = max(maxAttack, attack)
            minAttack = min(minAttack, attack)

        prev = maxDefense[maxAttack]
        for i in reversed(range(maxAttack + 1)):
            if i not in maxDefense:
                continue

            maxDefense[i] = max(maxDefense[i], prev)
            prev = maxDefense[i]

        weakCharacters = 0
        for attack, defense in properties:

            if defense < maxDefense[attack]:
                weakCharacters += 1
        return weakCharacters

    def numberOfWeakCharacters2(self, properties: List[List[int]]) -> int:



properties = [[5, 5], [6, 3], [3, 6]]
properties = [[2, 2], [3, 3]]
properties = [[1, 5], [10, 4], [4, 3]]
properties = [[1, 1], [2, 1], [2, 2], [1, 2]]
test = Solution()
print(test.numberOfWeakCharacters(properties))
print(test.numberOfWeakCharacters2(properties))

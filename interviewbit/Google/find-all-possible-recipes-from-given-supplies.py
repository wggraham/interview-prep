from typing import List
from copy import copy

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)

        s = set()
        for i in range(len(ingredients)):
            ingredients[i] = set(ingredients[i]).difference(supplies)
            if not ingredients[i]:
                supplies.add(recipes[i])
                s.add(recipes[i])

        res = copy(s)
        while s:
            ingredient = s.pop()
            for i in range(len(ingredients)):
                if ingredient in ingredients[i]:
                    ingredients[i].remove(ingredient)
                    if not ingredients[i]:
                        s.add(recipes[i])
                        res.add(recipes[i])
        return res


recipes = ["bread"]
ingredients = [["yeast","flour"]]
supplies = ["yeast","flour","corn"]
test = Solution()
print(test.findAllRecipes(recipes, ingredients, supplies))

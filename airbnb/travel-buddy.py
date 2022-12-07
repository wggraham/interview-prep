from heapq import *


class TravelBuddy:
    BUDDY_THRESHOLD = 0.5

    @staticmethod
    def find_travel_buddies(my_wish_list, my_friends_wish_lists):
        if not my_wish_list or not my_friends_wish_lists:
            return

        buddies = []
        for i, lst in enumerate(my_friends_wish_lists):
            common = my_wish_list.intersection(lst)
            percentage = len(common) / len(lst)
            if percentage > TravelBuddy.BUDDY_THRESHOLD:
                buddies.append((-percentage, i))

        buddies.sort()
        res = []
        for _, i in buddies:
            res.append(my_friends_wish_lists[i])

        return res


mine = {"a", "b", "c", "d"}
friends = [
    {"a", "b", "e", "f"},
    {"a", "c", "d", "g"},
    {"c", "f", "e", "g"},
]

print(TravelBuddy.find_travel_buddies(mine, friends))


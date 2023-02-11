from collections import defaultdict, deque, Counter
from itertools import combinations
from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        patterns, n, i, longest, res = defaultdict(set), len(timestamp), 0, 0, None

        while i < n:
            name = username[i]
            q = deque()
            while i < n and username[i] == name:
                q.append(website[i])
                i += 1
                if len(q) < 3: continue
                if len(q) > 3:
                    q.popleft()
                p = tuple(q)
                patterns[p].add(name)

        for p in sorted(patterns.keys()):
            if len(patterns[p]) > longest:
                longest = len(patterns[p])
                res = p

        return list(res) if res else []

    def mostVisitedPattern2(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        patterns, n, i, longest, res = defaultdict(set), len(timestamp), 0, 0, None

        visited = sorted(zip(timestamp, username, website))
        user_visit_map = defaultdict(list)
        for _, name, site in visited:
            user_visit_map[name].append(site)

        for name, sites in user_visit_map.items():
            q = deque()
            for site in sites:
                q.append(site)
                if len(q) < 3: continue
                if len(q) > 3:
                    q.popleft()
                p = tuple(q)
                patterns[p].add(name)

        for p in sorted(patterns.keys()):
            if len(patterns[p]) > longest:
                longest = len(patterns[p])
                res = p

        return list(sorted(res)) if res else []

    def mostVisitedPattern3(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        patterns, n, i, longest, res = defaultdict(set), len(timestamp), 0, 0, None

        visited = sorted(zip(timestamp, username, website))
        user_visit_map = defaultdict(list)
        for _, name, site in visited:
            user_visit_map[name].append(site)

        def gen_combos(i, combo):
            nonlocal sites, name, n
            if len(combo) == 3:
                patterns[tuple(combo)].add(name)
                return
            for j in range(i, n):
                gen_combos(j + 1, combo + [sites[j]])

        for name, sites in user_visit_map.items():
            n = len(sites)
            gen_combos(0, [])

        for p in sorted(patterns.keys()):
            if len(patterns[p]) > longest:
                longest = len(patterns[p])
                res = p

        return res

    def mostVisitedPattern4(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        patterns, n, i, longest, res = Counter(), len(timestamp), 0, 0, None

        visited = sorted(zip(timestamp, username, website))
        user_visit_map = defaultdict(list)
        for _, name, site in visited:
            user_visit_map[name].append(site)

        for name, sites in user_visit_map.items():
            patterns.update(Counter(set(combinations(sites, 3))))

        for p in sorted(patterns.keys()):
            if patterns[p] > longest:
                longest = patterns[p]
                res = p

        # return max(sorted(patterns), key=patterns.get)
        return res

    def mostVisitedPattern5(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        patterns, longest, res, visited = defaultdict(set), 0, None, sorted(zip(username, timestamp, website))

        prev_name, sites = visited[0][0], []
        for name, _, site in visited:
            if name != prev_name:
                for combo in combinations(sites, 3):
                    patterns[combo].add(prev_name)
                sites = []
                prev_name = name
            sites.append(site)

        for combo in combinations(sites, 3):
            patterns[combo].add(prev_name)

        for p in sorted(patterns.keys()):
            if len(patterns[p]) > longest:
                longest = len(patterns[p])
                res = p

        return res

    def mostVisitedPattern6(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        patterns, longest, res = Counter(), 0, None

        user_visit_map = defaultdict(list)
        for _, name, site in sorted(zip(timestamp, username, website)):
            user_visit_map[name].append(site)

        for name, sites in user_visit_map.items():
            patterns.update(Counter(set(combinations(sites, 3))))

        return max(sorted(patterns), key=patterns.get)

    def mostVisitedPattern7(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        patterns, longest, res, visited = Counter(), 0, None, sorted(zip(username, timestamp, website))

        prev_name, sites = visited[0][0], []
        for name, _, site in visited + [('', 0, '')]:
            if name != prev_name:
                patterns.update(Counter(set(combinations(sites, 3))))
                sites = []
                prev_name = name
            sites.append(site)

        return max(sorted(patterns), key=patterns.get)


username = ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"]
timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
website = ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]

username = ["ua", "ua", "ua", "ub", "ub", "ub"]
timestamp = [1, 2, 3, 4, 5, 6]
website = ["a", "b", "a", "a", "b", "c"]

username = ["zkiikgv", "zkiikgv", "zkiikgv", "zkiikgv"]
timestamp = [436363475, 710406388, 386655081, 797150921]
website = ["wnaaxbfhxp", "mryxsjc", "oz", "wlarkzzqht"]

username = ["h", "eiy", "cq", "h", "cq", "txldsscx", "cq", "txldsscx", "h", "cq", "cq"]
timestamp = [527896567, 334462937, 517687281, 134127993, 859112386, 159548699, 51100299, 444082139, 926837079,
             317455832, 411747930]
website = ["hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi",
           "yljmntrclw", "hibympufi", "yljmntrclw"]

test = Solution()
print(test.mostVisitedPattern2(username, timestamp, website))
print(test.mostVisitedPattern3(username, timestamp, website))
print(test.mostVisitedPattern4(username, timestamp, website))
print(test.mostVisitedPattern5(username, timestamp, website))
print(test.mostVisitedPattern6(username, timestamp, website))
print(test.mostVisitedPattern7(username, timestamp, website))

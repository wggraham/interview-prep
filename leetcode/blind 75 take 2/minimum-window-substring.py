from sys import maxsize
from collections import Counter, deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = Counter(t)
        total = len(t)
        window = Counter()
        i, j = 0, 0

        for i, c in enumerate(s):
            if c not in counts:
                continue

            window[c] += 1
            if window[c] == counts[c]:
                total -= counts[c]
            if total == 0:
                break

        if total:
            return ""
        while s[j] not in counts: j += 1

        total = len(s)
        res = (0, 0)
        while i < (len(s) - 1):
            if i - j < total and counts.total() <= (i - j):
                total = i - j
                res = (j, i)
            # need to remove 1 character present in t
            # then remove all characters after it not in t, until j index reaches another character in t
            while j < len(s) and s[j] in counts and window[s[j]] >= counts[s[j]]:
                window[s[j]] -= 1
                j += 1
            k = j - 1
            # remove characters until a single 1 from t encountered, remove it, then continue removing chars until another char in t is hit
            while j < len(s) and s[j] not in counts:
                j += 1

            i += 1
            while i < len(s) and window[s[k]] < counts[s[k]]:
                if s[i] in counts:
                    window[s[i]] += 1
                i += 1
            i -= 1

        while j < len(s) and s[j] in counts and window[s[j]] > counts[s[j]]:
            window[s[j]] -= 1
            j += 1
        if i - j < total and counts.total() <= (i - j + 1):
            res = (j, i)
        return s[res[0]:res[1] + 1]

    def minWindow2(self, s, t):
        counts = Counter(t)
        required = len(counts)
        j, i = 0, 0
        window = Counter()  # keeps count of all the unique characters in the current window.

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # ans tuple of the form (window length, left, right)
        ans = maxsize, None, None

        while i < len(s):
            # Add one character from the right to the window
            c = s[i]
            window[c] += 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if c in counts and window[c] == counts[c]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while j <= i and formed == required:
                c = s[j]

                # Save the smallest window until now.
                if i - j + 1 < ans[0]:
                    ans = (i - j + 1, j, i)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window[c] -= 1
                if c in counts and window[c] < counts[c]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                j += 1

                # Keep expanding the window once we are done contracting.
            i += 1
        return "" if ans[0] == maxsize else s[ans[1]: ans[2] + 1]

    def minWindow3(self, s, t):
        counts = Counter(t)
        required = len(counts)

        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
        filtered_s = []
        for i, c in enumerate(s):
            if c in counts:
                filtered_s.append((i, c))

        j, i = 0, 0
        formed = 0
        window = Counter()
        ans = maxsize, None, None

        # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
        # Hence, we follow the sliding window approach on as small list.
        while i < len(filtered_s):
            c = filtered_s[i][1]
            window[c] = window.get(c, 0) + 1

            if window[c] == counts[c]:
                formed += 1

            # If the current window has all the characters in desired frequencies i.e. t is present in the window
            while j <= i and formed == required:
                c = filtered_s[j][1]

                # Save the smallest window until now.
                end = filtered_s[i][0]
                start = filtered_s[j][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                window[c] -= 1
                if window[c] < counts[c]:
                    formed -= 1
                j += 1

            i += 1
        return "" if ans[0] == maxsize else s[ans[1]: ans[2] + 1]

    def minWindow4(self, s: str, t: str) -> str:
        # get counts of chars in t
        t_counts = Counter(t)
        # create a counter for keeping track of chars in w
        w = Counter()
        # keep track of shortest answer found so far
        r = ''
        # keep track of which characters we have in the current window
        window = deque()
        for ch in s:
            # add current character to window
            window.append(ch)
            # increment count in window
            w[ch] += 1
            # check if predicate is satisfied (window contains all chars in t)
            if all(w[c] >= t_counts[c] for c in t_counts.keys()):
                # remove unnecessary (superfluous) chars
                while window and w[window[0]] > t_counts[window[0]]:
                    w[window.popleft()] -= 1
                # record this new answer only if it is shorter than a previous answer
                # (or if no previous answer exists)
                if r == '' or len(window) < len(r):
                    r = ''.join(window)
                # remove the last added char so we can keep looking for more substrings
                if window:
                    w[window.popleft()] -= 1

        return r

    def minWindow5(self, s: str, t: str) -> str:
        # get counts of chars in t
        counts = Counter(t)
        # create a counter for keeping track of chars in w
        w = Counter()
        # keep track of shortest answer found so far
        r = ''
        # keep track of which characters we have in the current window
        window = deque()
        total = len(t)
        for ch in s:
            # add current character to window
            window.append(ch)
            # increment count in window
            if ch in counts:
                w[ch] += 1
                if w[ch] == counts[ch]:
                    total -= counts[ch]
            # check if predicate is satisfied (window contains all chars in t)
            if total <= 0:
                # remove unnecessary (superfluous) chars
                while window and w[window[0]] > counts[window[0]]:
                    w[window.popleft()] -= 1
                # record this new answer only if it is shorter than a previous answer
                # (or if no previous answer exists)
                if r == '' or len(window) < len(r):
                    r = ''.join(window)
                # remove the last added char so we can keep looking for more substrings
                if window:
                    w[window.popleft()] -= 1

        return r

    def minWindow6(self, s: str, t: str) -> str:
        def shrink(idx, includeEssential=False):
            nonlocal counts, window
            lastEssentialIndex = idx
            if includeEssential:
                while idx < len(s) and (s[idx] not in counts or (s[idx] in counts and window[s[idx]] >= counts[s[idx]])):
                    if s[idx] in counts:
                        window[s[idx]] -= 1
                        lastEssentialIndex = idx
                    idx += 1
            else:
                while idx < len(s) and (s[idx] not in counts or (s[idx] in counts and window[s[idx]] > counts[s[idx]])):
                    if s[idx] in counts:
                        window[s[idx]] -= 1
                    idx += 1
            return idx, lastEssentialIndex

        counts = Counter(t)
        total = len(t)
        window = Counter()
        i, j = 0, 0

        for i, c in enumerate(s):
            if c not in counts:
                continue

            window[c] += 1
            if window[c] == counts[c]:
                total -= counts[c]
            if total == 0:
                break

        if total:
            return ""

        j, _ = shrink(0)
        total = i - j + 1
        res = (j, i)

        while i < (len(s) - 1):
            if total > (i - j + 1) >= len(t):
                total = i - j + 1
                res = (j, i)
            j, k = shrink(j, True)

            i += 1
            while i < len(s) and window[s[k]] < counts[s[k]]:
                if s[i] in counts:
                    window[s[i]] += 1
                i += 1

        j, _ = shrink(j)
        if total > (i - j + 1) >= len(t):
            res = (j, i)

        return s[res[0]:res[1] + 1]


s = "ADOBECODEBANC"
t = "ABC"
# s = "bancbca"
# t = "abc"
# s = "abc"
# t = "b"
s = "ab"
t = "b"

s = "bdab"
t = "ab"
test = Solution()
print(test.minWindow6(s, t))

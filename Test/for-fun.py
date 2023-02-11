from collections import Counter


def anagrams_name(name, words):
    count, name_count = 0, tuple(sorted(Counter(c for c in name).items()))

    for word in words:
        if len(name) != len(word): continue
        char_counts = tuple(sorted(Counter(c for c in word).items()))
        count += name_count == char_counts

    return count


a = "testing"
b = ["testing", "fool", "ttingesttt"]
print(anagrams_name(a, b))

def count_words(text):
    return len(text.split())

def count_characters(text):
    counts = dict()
    lower = text.lower()
    for c in lower:
        if not c in counts:
            counts[c] = 0
        counts[c] += 1
    return counts

def sort_key(d):
    return d["count"]

def sort_characters_by_counts(counts):
    l = []
    for char in counts:
        l.append({"char": char, "count": counts[char]})
    l.sort(reverse=True, key=sort_key)
    return l

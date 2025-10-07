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


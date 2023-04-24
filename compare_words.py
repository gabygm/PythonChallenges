def misspelled(word1, word2):
    l1, l2 = len(word1), len(word2)
    if l1 == l2:
        return sum(1 for key, value in zip(word1, word2) if key != value) <= 1
    elif l1 - l2 == 1:
        return word1.startswith(word2) or word1.endswith(word2)
    elif l1 - l2 == -1:
        return word2.startswith(word1) or word2.endswith(word1)
    return False

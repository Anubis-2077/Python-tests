from collections import Counter

words = ["ABETTOR", "ABILITIES", "PALMED", "VALVED", "VAMPED", "ABILITY"]


from collections import Counter


def longest_word(letters):

    possible_words = [word for word in words if not (Counter(word) - Counter(letters))]

    if not possible_words:
        return None

    possible_words.sort(key=lambda x: (-len(x), x))
    max_length = len(possible_words[0])
    longest_words = [word for word in possible_words if len(word) == max_length]

    return longest_words

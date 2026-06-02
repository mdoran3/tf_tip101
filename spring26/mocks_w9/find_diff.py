# Problem - Find the Difference
# Given two strings s and t, where t is s shuffled with one extra letter added,
# return the letter that was added to t.

from collections import Counter

def find_the_difference(s, t):
    counts = Counter(s)
    for ch in t:
        counts[ch] -= 1
        if counts[ch] < 0:
            return ch


if __name__ == "__main__":
    print(find_the_difference("abcd", "abcde"))  # 'e'
    print(find_the_difference("", "y"))           # 'y'
    print(find_the_difference("a", "aa"))          # 'a'

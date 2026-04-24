# Problem #2 - Ransom Note
# Given two strings ransomNote and magazine, return True if ransomNote
# can be constructed by using the letters from magazine and False otherwise.

# Each letter in magazine can only be used once in ransomNote.

from collections import Counter

def can_construct(ransomNote, magazine):
    counts = Counter(magazine)
    for ch in ransomNote:
        if counts[ch] <= 0:
            return False
        counts[ch] -= 1
    return True


if __name__ == "__main__":
    print(can_construct("aa", "aab"))   # True
    print(can_construct("aa", "ab"))    # False
    print(can_construct("a", "b"))      # False

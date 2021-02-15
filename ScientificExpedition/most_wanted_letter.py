#!/home/fode4cun/.local/share/virtualenvs/checkio-ufRDicT7/bin/checkio --domain=py run most-wanted-letter

# You are given a text, which contains different English letters and punctuation symbols.    You should find the most frequent letter in the text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, so for the purpose of your search,    "A" == "a".    Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
# 
# If you havetwo or more letters with the same frequency,    then return the letter which comes first in the Latin alphabet.    For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".
# 
# Input:A text for analysis as a string.
# 
# Output:The most frequent letter in lower case as a string.
# 
# Precondition:
# A text contains only ASCII symbols.
# 0 < len(text) ≤ 105
# 
# 
# END_DESC
import bisect
import re
from collections import Counter, defaultdict
from itertools import takewhile
from operator import itemgetter
from string import ascii_letters


def checkio(text: str) -> str:
    only_letters = re.findall(r'[a-zA-Z]+', text)
    c = Counter(''.join(only_letters).lower())
    max_val = c.most_common(1)[0][1]
    multiple_vals = list(takewhile(lambda x: x[1] == max_val, c.most_common()))
    return sorted(multiple_vals, key=itemgetter(0))[0][0]


# def checkio(text: str) -> str:
#     keys = defaultdict(int)

#     for l in text.lower():
#         if l in ascii_letters:
#             keys[l] += 1

#     max_val = max(keys.values())
#     return sorted([k for k, v in keys.items() if v == max_val])[0]


# def checkio(text: str) -> str:
#     keys = defaultdict(int)

#     for l in text.lower():
#         if l in ascii_letters:
#             keys[l] += 1

#     max_val = max(keys.values())
#     sorted_list = []

#     for k, v in keys.items():
#         if v == max_val:
#             bisect.insort(sorted_list, k)

#     return sorted_list[0]



if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

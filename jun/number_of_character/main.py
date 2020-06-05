"""
Input: 'This is a pen. This is an apple. Applepen.'
Output: ('pf, 6')
"""
import operator
from typing import Tuple


def count_chars_v1(strings: str) -> Tuple[str, int]:
    strings = strings.lower()
    l = []
    for char in strings:
        if not char.isspace():
            l.append((char, strings.count(char)))

    return max(l, key=operator.itemgetter(1))


if __name__ ==  '__main__':
    s = 'This is a pen. This is an apple. Applepen.'
    print(count_chars_v1(s))
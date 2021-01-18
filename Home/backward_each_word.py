#!/home/fode4cun/.local/share/virtualenvs/checkio-ufRDicT7/bin/checkio --domain=py run backward-each-word

# In a given string you should reverse every word, but the words should stay in their places.
# 
# Input:A string.
# 
# Output:A string.
# 
# Precondition:The line consists only from alphabetical symbols and spaces.
# 
# 
# END_DESC
import re

def backward_string_by_word(text: str) -> str:
    return ' '.join(i[::-1] for i in re.split(r'\W', text))

if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")

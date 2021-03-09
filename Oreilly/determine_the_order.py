#!/home/fode4cun/.local/share/virtualenvs/checkio-ufRDicT7/bin/checkio --domain=py run determine-the-order

# The Robots have found an encrypted message. We cannot decrypt it at the moment,    but we can take the first steps towards doing so. You have a set of "words", all in lower case, and each word contains    symbols in "alphabetical order". (it's not your typical alphabetical order, but a new and different order.)    We need to determine the order of the symbols from each "word" and create a single "word" with all of these symbols,    placing them in the new alphabetical order.    In some cases, if we cannot determine the order for several symbols, you should use the traditionallatin alphabetical        order.    For example:    Given words "acb", "bd", "zwa". As we can see "z" and "w" must be before "a"    and "d" after "b". So the result is "zwacbd".Input:Words as a list of strings.
#
# Output:The order as a string.
#
# Precondition:For each test, there can be the only one solution.
# 0<|words|<10
#
#
# END_DESC
def checkio(words):
    # Unique alphabet
    alphabet = sorted(set(''.join(words)))
    result = ''

    for _ in range(len(alphabet)):
        # Find minimum
        for c in alphabet:
            if c in result:
                # Already used
                continue
            if all(c not in word or c == word[0] for word in words):
                # Found
                break

        result += c
        # Remove c from words
        for i in range(len(words)):
            words[i] = words[i].replace(c, '')

    return result


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(['my', 'name', 'myke']) == "namyke"
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(['hello', 'low', 'lino', 'itttnosw']) == 'helitnosw', \
        'helow / helinow / helitnosw'
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"

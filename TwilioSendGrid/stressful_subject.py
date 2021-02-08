#!/home/fode4cun/.local/share/virtualenvs/checkio-ufRDicT7/bin/checkio --domain=py run stressful-subject

# 
# END_DESC
import re

def is_stressful(subj):
    """
        recognize stressful subject
    """
    if subj.isupper() or subj.endswith('!!!'):
        return True

    patterns = [r'(\b[help\!\-\.]{4,}\b)', r'(\b[asap\!\-\.]{4,}\b)', r'(\b[urgent\!\-\.]{4,}\b)']

    for pattern in patterns:
        if re.search(pattern, subj, flags=re.IGNORECASE):
            return True

    return False

if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')

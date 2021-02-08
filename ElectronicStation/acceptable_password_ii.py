#!/home/fode4cun/.local/share/virtualenvs/checkio-ufRDicT7/bin/checkio --domain=py run acceptable-password-ii

# In this mission you need to create a password verification function.
# 
# Those are the verification conditions:
# 
# the length should be bigger than 6;should contain at least one digit.Input:A string.
# 
# Output:A bool.
# 
# 
# END_DESC

# Taken from mission Acceptable Password I




#

#

#

#

#
#


def is_acceptable_password(password: str) -> bool:
    return len(password) > 6 and any(c.isdigit() for c in password)


if __name__ == '__main__':
    print("Example:")
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

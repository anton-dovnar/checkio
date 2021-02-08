#!/home/fode4cun/.local/share/virtualenvs/checkio-ufRDicT7/bin/checkio --domain=py run lightbulb-start-watching

# This is the second mission in the lightbulb series. I will try to make each following task slightly more complex.
#
# You have already learned how to count the amount of time a light bulb has been on, or how long a room has been lit. Now let's add one more parameter - the counting start time.
#
# This means that the light continues to turn on and off as before. But now, as a result of the function, I want not only to know how long there was light in the room, but how long the room was lit, starting from a certain moment.
#
# One more argument is added –start_watching, and if it’s not passed, we count as in the previous version of the program for the entire period.
#
# Input:Two arguments and only the first one is required. The first one is a list of datetime objects and the second one is a datetime object.
#
# Output:A number of seconds as an integer.
#
# Precondition:
#
# The array of pressing the button is always sorted in ascending orderThe array of pressing the button has no repeated elementsThe amount of elements is always even (the light will eventually be off)The minimum possible date is 1970-01-01The maximum possible date is 9999-12-31
# END_DESC

# Taken from mission Lightbulb Intro


















from datetime import datetime
from typing import List

def sum_light(els: List[datetime]) -> int:
    """
        how long the light bulb has been turned on
    """
    time = []

    for i in range(0, len(els), 2):
        time.append((els[i+1] - els[i]).total_seconds())

    return sum(time)


if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
    ]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
    ]) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
    ]) == 1220

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 10 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 12, 11, 10 , 10),
        datetime(2015, 1, 12, 11, 10 , 10),
        datetime(2015, 1, 12, 12, 10 , 10),
    ]) == 4820

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 0 , 1),
    ]) == 1

    assert sum_light([
        datetime(2015, 1, 12, 10, 0 , 0),
        datetime(2015, 1, 12, 10, 0 , 10),
        datetime(2015, 1, 12, 11, 0 , 0),
        datetime(2015, 1, 13, 11, 0 , 0),
    ]) == 86410

    print("The first mission in series is completed? Click 'Check' to earn cool rewards!")


from datetime import datetime
from typing import List, Optional

def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    """
        how long the light bulb has been turned on
    """
    if not start_watching:
        return sum([(els[i+1] - els[i]).total_seconds() for i in range(0, len(els), 2)])

    time = []

    for i in range(0, len(els), 2):
        if els[i] <= start_watching <= els[i+1]:
            time.append((els[i + 1] - start_watching).total_seconds())
        elif els[i] > start_watching and not time:
            continue
        elif els[i+1] > start_watching:
            time.append((els[i + 1] - els[i]).total_seconds())

    return sum(time)


if __name__ == '__main__':
    print("Example:")
    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 11),
        datetime(2015, 1, 12, 12, 10, 11)], datetime(2015, 1, 12, 11, 10, 0)))

    print(sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
    datetime(2015, 1, 12, 10, 0, 5)))

    assert sum_light(els=[
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ],
    start_watching=datetime(2015, 1, 12, 10, 0, 5)) == 5

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 0, 10),
    ], datetime(2015, 1, 12, 10, 0, 0)) == 10

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 11, 0, 0)) == 610

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 11, 0, 10)) == 600

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
    ], datetime(2015, 1, 12, 10, 10, 0)) == 620

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 11),
        datetime(2015, 1, 12, 12, 10, 11),
    ], datetime(2015, 1, 12, 12, 10, 11)) == 0

    assert sum_light([
        datetime(2015, 1, 12, 10, 0, 0),
        datetime(2015, 1, 12, 10, 10, 10),
        datetime(2015, 1, 12, 11, 0, 0),
        datetime(2015, 1, 12, 11, 10, 10),
        datetime(2015, 1, 12, 11, 10, 11),
        datetime(2015, 1, 12, 12, 10, 11),
    ], datetime(2015, 1, 12, 12, 9, 11)) == 60

    print("The second mission in series is done? Click 'Check' to earn cool rewards!")

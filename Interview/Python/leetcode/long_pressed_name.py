#Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

#You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

def get_next_different_letter_pos(long_pressed_name, long_index):
    count = len(long_pressed_name)
    index = 0
    for i in range (long_index, count - 1):
        if long_pressed_name[i] == long_pressed_name[i+1]:
            index += 1
        else:
            return (i + 1)
    return -1


def is_long_pressed(name, long_pressed_name):
    count = len(long_pressed_name)
    long_index = 0
    for i in range(count):
        if (name[i] == long_pressed_name[long_index]):
            long_index += 1
            continue

        if (long_pressed_name[long_index - 1] == long_pressed_name[long_index]):
            long_index = get_next_different_letter_pos(long_pressed_name, long_index)
            if long_index == -1:
                return False
            if (name[i] == long_pressed_name[long_index]):
                long_index += 1
                continue

        return False

    return True

def isLongPressedName(name, typed):
    from itertools import groupby
    grouped_name = groupby(typed)
    for it in grouped_name:
        print(it[0], list(it[1]))
    name_groups = [(ch, len(list(g))) for ch, g in groupby(name)]
    typed_groups = [(ch, len(list(g))) for ch, g in groupby(typed)]
    if len(typed_groups) != len(name_groups):
        return False
    for i in range(len(name_groups)):
        if typed_groups[i][0] != name_groups[i][0] or \
            typed_groups[i][1] < name_groups[i][1]:
            return False
    return True


print(isLongPressedName("jackson", "jjacksoonnn"))
#Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

def is_constructed_from_substring(s:str)->bool:
    count = len(s)
    if count <= 1:
        return False

    for i in range(1, count):
        substr = s[:i]
        repeat_count = count // i
        composed_string = ""
        for j in range(repeat_count):
            composed_string = composed_string + substr
#            print(composed_string)
        if composed_string == s:
            return True

 #       print (substr)
    return False

s = "abab"
print (is_constructed_from_substring(s))

s = "ababa"
print (is_constructed_from_substring(s))

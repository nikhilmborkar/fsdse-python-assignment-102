def is_rotation(s1,s2):
    if s1 == None or s2 == None:
        return False
    if s1 == '':
        if s2 == '':
            return True
        return False

    for index in range(len(s1)):
        if s1[index:]+s1[0:index] == s2:
            return True
    return False

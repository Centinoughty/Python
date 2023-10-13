def swap_case(s):
    listed = list(s)
    result = ""
    for i in range(0, len(listed)):
        if listed[i].isupper() == True:
            listed[i] = listed[i].lower()
        else:
            listed[i] = listed[i].upper()
        result += listed[i]
    return result

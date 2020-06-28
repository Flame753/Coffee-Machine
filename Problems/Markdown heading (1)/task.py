def heading(text, level=0):
    hsh = "#"
    text = " " + text
    if level <= 1:
        return hsh * 1 + text
    elif level >= 6:
        return hsh * 6 + text
    else:
        return hsh * level + text
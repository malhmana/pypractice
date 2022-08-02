def wrap(string, max_width):
    new_string= ""
    num= 0
    while num < len(string):
        if num == 0 or num % max_width != 0:
            new_string += string[num]
            num  += 1
        else:
            new_string += '\n' + string[num]
            num += 1
    return new_string

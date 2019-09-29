def swap_case(string):
    swaped_string = ''
    for i in range(0, len(string)):
        if string[i].islower():
            swaped_string += string[i].upper()
        else:
            swaped_string += string[i].lower()
    return swaped_string


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

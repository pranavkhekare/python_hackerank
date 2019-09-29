def minion_game(string):
    stuart_string = 0
    kevin_string = 0
    for i in range(0, len(string)):
        if string[i] in ('A', 'E', 'I', 'O', 'U'):
            kevin_string += len(string) - i
        else:
            stuart_string += len(string) - i
    if kevin_string > stuart_string:
        print('Kevin', kevin_string)
    elif stuart_string > kevin_string:
        print('Stuart', stuart_string)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)

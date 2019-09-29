def mutate_string(string, position, character):
    return print(string[:position]+character+string[position+1:])


if __name__ == '__main__':
    string = input()
    inp = input().split()
    mutate_string(string, int(inp[0]), inp[1])

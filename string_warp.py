import textwrap

def wrap(string, max_width):
    warp = textwrap.wrap(string, max_width)
    return warp


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    for i in result:
        print(i)

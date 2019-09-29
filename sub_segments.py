import textwrap

def merge_the_tools(string, k):
    list = textwrap.wrap(string, k)
    for i in list:
        word = ''
        for j in range(len(i)):
            if word == '':
                word = i[j]
            elif i[j] not in word:
                word += i[j]
            else:
                continue
        print(word)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

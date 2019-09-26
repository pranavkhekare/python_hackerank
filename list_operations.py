n = int(input())
list = []

for x in range(1, n):
    temp_list = input(). split()
    if temp_list[0] == 'insert':
        list.insert(int(temp_list[1]), int(temp_list[2]))
    elif temp_list[0] =='print':
        print(list)
    elif temp_list[0] == 'remove':
        list.remove(int(temp_list[1]))
    elif temp_list[0] =='append':
        list.append(int(temp_list[1]))
    elif temp_list[0] == 'sort':
        list.sort()
    elif temp_list[0] =='pop':
        list.pop()
    elif temp_list[0] =='reverse':
        list.reverse()
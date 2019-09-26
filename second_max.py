number = int(input())
inp = [int(x) for x in input().split()]
inp = sorted(set(inp))[-2]

print(inp)
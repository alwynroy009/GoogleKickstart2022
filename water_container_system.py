
# Water Container System
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb409/0000000000bef79e
# (Problem Explanation) Part 1 - https://youtu.be/xo4Tbs6JABQ
# (Code Explanation) part 2 - https://youtu.be/5uu6FCcg-Qc

for tests in range(1, int(input()) + 1):
    N, Q  = map(int, input().split())
    connections = {i:set() for i in range(1, N+1)}
    for _ in range(N-1):
        i , j = map(int, input().split())
        connections[i].add(j)
        connections[j].add(i)
    # print(connections)
    for _ in range(Q):
        input()
    checked = {1}
    level = [1]
    capacity = []
    while level:
        capacity.append(len(level)) 
        new_L = []
        for i in level:
            for j in connections[i]:
                if j in checked:
                    continue
                checked.add(j)
                new_L.append(j)
            level = new_L
    # print(capacity)
    result = 0
    for c in capacity:
        if result+c > Q:
            break
        result += c
    print(f'Case #{tests}: {result}')

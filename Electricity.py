# Problem Statement
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb1b6/0000000000c47c8e
# Explanation
https://youtu.be/D2EkHiB5SAI


import sys
sys.setrecursionlimit(2*(10**5))

def get_connections(conn, junctions, curr):
    if junctions[curr] != 0: return junctions[curr]
    junctions[curr] = 1
    for adj in conn[curr]:
        junctions[curr] += get_connections(conn, junctions, adj)
    return junctions[curr]

for test_case in range(1, int(input())+1):
    N = int(input())
    A = list(map(int, input().split()))
    conn = {i: set() for i in range(N)}
    for _ in range(N-1):
        node1, node2 = map(int, input().split())
        if A[node1-1] == A[node2-1]:
            continue
        if A[node1-1] < A[node2-1]:
            conn[node2-1].add(node1-1)
        else:
            conn[node1-1].add(node2-1)
    junctions = [0] * N
    for curr in range(N):
        junctions[curr] = get_connections(conn, junctions, curr)
    
    print(f'Case #{test_case}: {max(junctions)}')

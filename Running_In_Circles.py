# Problem Statement
https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb1b6/0000000000c4766e

# Problem Explanation
https://youtu.be/ONN7ZhlWx84

# Code Explanation
https://youtu.be/IBlg2NMY4ss

for test_case in range(1, int(input()) + 1):
    L , N = map(int, input().split())

    counter = 0
    position = 0

    for _ in range(N):
        dist, dir = input().split()
        dist = int(dist)

        if dir == 'C':
            position += dist
        else:
            position -= dist
        cnt = abs(position) // L
        if position < 0:
            position = -1 * (abs(position) % L)
        else:
            position = abs(position) % L
        counter += cnt 
        
    print(f"Case #{test_case}: {counter}")

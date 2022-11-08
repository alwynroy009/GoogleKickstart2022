# Problem Statement : https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb2e1/0000000000c17c82
# Problem Explanation : https://youtu.be/QwxgIJhWneE
# Code Explanation : (Work in progress)

from math import sqrt

for tests in range(1, int(input())+1):
    R_stone, R_home = map(int, input().split())
    R_total = R_stone + R_home
    # Red stones
    r_distances = []
    for _ in range(int(input())):
        x, y = map(int, input().split())
        r_distances.append(sqrt(x**2 + y**2))
    # Yellow stones
    y_distances = []
    for _ in range(int(input())):
        x, y = map(int, input().split())
        y_distances.append(sqrt(x**2 + y**2))

    R_min, Y_min = float("inf"), float("inf")
    try:
        R_min, Y_min = min(r_distances), min(y_distances)
    except:
        pass
    
    R_win, Y_win = 0, 0
    for dist in r_distances:
        if dist<=min(Y_min-0.0001,R_total):
            R_win += 1

    for dist in y_distances:
        if dist<=min(R_min-0.0001,R_total):
            Y_win += 1

    print(f'Case #{tests}: {R_win} {Y_win}')

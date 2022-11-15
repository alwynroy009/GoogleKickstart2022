####### Problem Statement
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb1b6/0000000000c47e79

####### Explanation
# https://youtu.be/8SvnF_NdjUA

L = 10**5
Ans = list(range(L+2))
for i in range(5, L+1):
    Ans[i+1] = min(Ans[i]+1, Ans[i+1])
    curr = Ans[i] + 4
    for j in range(2*i, L+1, i):
        curr += 2
        Ans[j] = min(Ans[j], curr)

for tests in range(1,int(input())+1):
    print(f'Case #{tests}: {Ans[int(input())]}')

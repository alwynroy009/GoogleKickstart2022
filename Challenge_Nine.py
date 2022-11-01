# Problem statement : https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7997
# Explanation : https://youtu.be/X7yIgMdBSgo

for t in range(1, int(input())+1):
    N = input()
    S = 0
    for digit in N:
        S += int(digit)
    if S % 9 == 0:
        x = 0
        ans = N[0]+'0'+N[1:]
    else:
        x = 9 - S % 9
        i = 0
        
        ans = ''
        while i < len(N) and int(N[i]) <= x:
            ans += N[i]
            i += 1
        ans += str(x)
        ans += N[i:]
        
    
    print(f'Case #{t}: {ans}')

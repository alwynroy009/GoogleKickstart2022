test_cases = int(input())

for t in range(test_cases):
    ip_str = input()
    test_str = input()
    ptr_ip, ptr_test = 0,0
    while ptr_ip < len(ip_str) and ptr_test < len(test_str):
        if ip_str[ptr_ip] == test_str[ptr_test]:
            ptr_ip += 1
            ptr_test += 1
        else:
            ptr_test += 1
    
    if ptr_ip == len(ip_str):
        ans = len(test_str) - len(ip_str)
    else:
        ans = 'IMPOSSIBLE'
    
    print(f'Case #{t+1}: {ans}')

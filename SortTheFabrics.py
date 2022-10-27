for tests in range(1,int(input())+1):
    fabrics = []
    no_fabrics = int(input())
    for i in range(no_fabrics):
        c, d, u = input().split()
        fabrics.append((c, int(d), int(u)))
    
    fabrics.sort(key=lambda x:x[2])
    Ada = fabrics 
    Charles = fabrics.copy() 
    
    Ada.sort(key=lambda x:x[0])
    Charles.sort(key=lambda x:x[1])
    tot_matches = 0
    for x,y in zip(Ada, Charles):
        if x == y:
            tot_matches += 1

    print(f'Case #{tests}: {tot_matches}')

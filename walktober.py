for case in range(1, int(input())+1):
    tot_part, days, john_ID = map(int, input().split())
    max_score = [0 for _ in range(days)]
    for part in range(1, tot_part+1):
        scores = list(map(int, input().split()))
        i = 0
        for s in scores:
            max_score[i] = max(max_score[i], s)
            i = i + 1
        if part == john_ID:
            john = scores
    answer = sum(m-j for m, j in zip(max_score, john))
    print(f'Case #{case}: {answer}')

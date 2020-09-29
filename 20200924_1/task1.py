print([i for i in range(1, int(input())) if all([i%d for d in range(2, i//2+1)])])

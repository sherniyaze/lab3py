import itertools

string_N = input()

permut = itertools.permutations(string_N)

print([''.join(p) for p in permut])
import itertools

characters = ['w', 'l', 'd']
length = 10

combinations = list(itertools.product(characters, repeat=length))

for combination in combinations:
    print(''.join(combination))

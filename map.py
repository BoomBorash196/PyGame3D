from settings import *

text_map = [
    'MMMMMMMMMMMM',
    'M..M.......M',
    'MM.M.......M',
    'M..M.M.M...M',
    'M........M.M',
    'M..M..M....M',
    'M.....M....M',
    'MMMMMMMMMMMM'
]

world_map = set()
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'M':
            world_map.add((i * TILE, j * TILE))
            mini_map.add((i * MAP_TILE, j * MAP_TILE))


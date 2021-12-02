with open('./Day20/D20_Input.txt') as f:
    lines = [line.rstrip() for line in f]

tiles = {}

def find_matches(current_id):
    matches_found = 0
    my_edges = tiles[current_id]
    for a, tile_id in enumerate(tile_ids):
        if tile_id == current_id:
            continue
        for edge in my_edges:
            if (edge in tiles[tile_id]) or (edge[::-1] in tiles[tile_id]):
                matches_found += 1
                break
    return matches_found


current_tile = []
for i, line in enumerate(lines):
    if i % 12 == 0:
        current_tile = []
        tile_id = line.split()[1][:-1]
    elif len(line) == 0:
        tile_edges = []
        tile_edges.append(current_tile[0])
        tile_edges.append(current_tile[9])
        for j in (0,9):
            temp = []
            for k in enumerate(current_tile):
                temp.append(k[1][j])
            tile_edges.append("".join(temp))
        tiles[tile_id] = tile_edges
    else:
        current_tile.append(line)

tile_ids = tiles.keys()
coner_pieces = []

for id in tile_ids:
    if find_matches(id) < 3:
        coner_pieces.append(id)

total = 1
for id in coner_pieces:
    total *= int(id)

print(total)
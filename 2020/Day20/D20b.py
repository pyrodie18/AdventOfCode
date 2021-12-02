with open('./Day20/D20_Input.txt') as f:
    lines = [line.rstrip() for line in f]

tiles = {}

def rotate_tile(tile):
    new_tile = []
    for i in range(len(tile[0])): 
        new_tile.append([x[i] for x in tile])
    return new_tile

def reverse_tile(tile):
    new_tile = []
    for row in tile:
        new_tile.append(row[::-1])
    return new_tile

def find_matches(current_id):
    matches_found = 0
    # Load up the tile we're searching for matches on
    the_tile = tiles[current_id]

    # Loop through each possible candidate
    for a, tile_id in enumerate(tile_ids):
        if tile_id == current_id:
            continue
        # Load Candidate Tile
        possible_tile = tiles[tile_id]
        # Loop through the_tile sides
        for b in range(4):
            # Loop through candiate tile sites
            for c in range(4):
                if the_tile[b]['pattern'] == possible_tile[c]['pattern']:
                    the_tile[b]['neighbor'] = (tile_id + '-' + str(c))
                    matches_found += 1
                elif the_tile[b]['pattern'][::-1] == possible_tile[c]['pattern']:
                    the_tile[b]['neighbor'] = (tile_id + '-' + str(c))
                    the_tile[b]['reverse'] = 0
                    matches_found += 1
        the_tile.append(matches_found)
        return the_tile


# Load each tile into tiles in the format
# TILE_ID: [{neighbor: #, reverse:0 , pattern: the pattern} x 3, [tile]]
current_tile = []
for i, line in enumerate(lines):
    if i % 12 == 0:
        current_tile = []
        tile_id = line.split()[1][:-1]
    elif len(line) == 0:
        tile_info = []
        tile_info.append({"neighbor": '', "reverse":0, "pattern": current_tile[0]})
        tile_info.append({"neighbor": '', "reverse":0, "pattern": current_tile[9]})
        for j in (0,9):
            temp = []
            for k in enumerate(current_tile):
                temp.append(k[1][j])
            tile_info.append({"neighbor": '', "reverse":0, "pattern": "".join(temp)})
        tile_info.append(current_tile)
        tiles[tile_id] = tile_info
    else:
        current_tile.append(line)

# Get a list of all the Tile IDs
tile_ids = tiles.keys()

# Loop Through Each Tile and replace it with a tile
# that contains the side mappings
for id in tile_ids:
    tiles[id] = find_matches(id)
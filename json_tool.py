import json, pathlib

def check_if_julia_cached_exists(x, y, cx, cy, R, max_iteration):
    if pathlib.Path(f'cached/{x}_{y}_{cx}_{cy}_{R}_{max_iteration}.json').is_file():
        print("Cache Found, Using Cache instead of re-calculating Julia Set.")
        return True
    else:
        return False
    
def write_julia_to_cache(x, y, cx, cy, R, max_iteration, julia_array):
    with open(f'cached/{x}_{y}_{cx}_{cy}_{R}_{max_iteration}.json', 'w') as json_file:
        json.dump(julia_array, json_file, indent=2)

def get_julia_from_cache(x, y, cx, cy, R, max_iteration):
    with open(f'cached/{x}_{y}_{cx}_{cy}_{R}_{max_iteration}.json', 'r') as json_file:
        iteration_map = json.load(json_file)

    return iteration_map
import json, os, glob, fire, shutil

ITEMS = (
    "clutter:common_coin_pouch",
    "clutter:uncommon_coin_pouch",
    "clutter:rare_coin_pouch",
    "clutter:epic_coin_pouch",
    "clutter:copper_coin",
    "clutter:silver_coin",
    "clutter:gold_coin",
)

def create_item(item, weight, min, max) -> dict:  
    return {
        "type": "minecraft:item",
        "name": item,
        "functions": [
        {
            "add": False,
            "count": {
            "type": "minecraft:uniform",
            "max": max,
            "min": min
            },
            "function": "minecraft:set_count"
        }
        ],
        "weight": weight
    }

def find_correct_loot_table(path, loot_table):
    found_ = []
    for subfolder in glob.glob(f'{path}*'):
        if os.path.isdir(subfolder):
            path = find_correct_loot_table(f'{subfolder}/', loot_table)
            if path is not None:
                found_.extend(path)
        elif loot_table in subfolder.split('/')[-1] and os.path.isfile(subfolder):
            found_.append(subfolder)
    return found_

def create_datapack():
    # Setup the folder structure
    if os.path.exists('./data'):
        shutil.rmtree('./data')
    os.makedirs('./data/')
    os.makedirs('./data/server_rp')
    os.makedirs('./data/server_rp/achievements')

    # Read the building rules
    with open('./rules.json', 'r') as file_:
        rules = json.load(file_)
    
    for namespace in rules:
        for subnamespace in os.listdir(f'./originals/{namespace}/data/'):
            loot_path = f'./originals/{namespace}/data/{subnamespace}/loot_tables/chests'
            if os.path.exists(loot_path):
                for loot_table, tables in rules[namespace].items():
                    # Find the files and copy them over
                    founds_ = find_correct_loot_table(loot_path, loot_table)
                    for found_ in founds_:
                        if found_:
                            path = './data/'
                            for folder_ in found_.split('/')[4:]: 
                                if 'json' not in folder_:
                                    path = f'{path}{folder_}/'
                                    os.makedirs(path, exist_ok=True)
                            shutil.copy(found_, path)
                            found_ = found_.replace(f'./originals/{namespace}/data/', './data/')
                            with open(found_, 'r') as file_:
                                old_loot_table = json.load(file_)
                            for table in tables:
                                old_loot_table["pools"][0]["entries"].append(create_item(table[0], table[1], table[2], table[3]))
                            with open(found_, 'w') as file_:
                                json.dump(old_loot_table, file_)

if __name__ == "__main__":
    fire.Fire(create_datapack)
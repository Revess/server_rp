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

def create_item(weight, min, max, item) -> dict:  
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

def create_set():
    # Setup the folder structure
    if os.path.exists('./data'):
        shutil.rmtree('./data')
    os.makedirs('./data/')
    for namespace in os.listdir('./originals'):
        os.makedirs(f'./data/{namespace}')
        os.makedirs(f'./data/{namespace}/loot_tables')
        os.makedirs(f'./data/{namespace}/loot_tables/chests')

    # Start building the loot tables
    

if __name__ == "__main__":
    fire.Fire(create_set)
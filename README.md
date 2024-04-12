minecraft: All
towns_and_towers: All
villagesandpillages: All
villagersplus: All
terralith:
    -underground/oak_cabin
    -sunken tower
    -underground_cabin
    -glacial_hut
    -fortified_village
    -fortified_desert_village
nova_cherry_village:
    -village_cherry
friendsandfoes:
    -citadel
    -iceologer_cabin
    -friendsandfoes:illusioner_shack
ctov: All

To test the loot, spam: ```/loot give @a loot (namespace):(loot)```

Example of adding to loot table:
add to the entries in the json the following:
```
{
          "type": "minecraft:item",
          "name": "clutter:common_coin_pouch",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "weight": 2
        },
        {
          "type": "minecraft:item",
          "name": "clutter:uncommon_coin_pouch",
          "functions": [
            {
              "add": false,
              "count": {
                "type": "minecraft:uniform",
                "max": 2.0,
                "min": 0.0
              },
              "function": "minecraft:set_count"
            }
          ],
          "weight": 1
        }
```
import json
import os
from os import path

if path.exists('./items'):
    print("Items folder already exists! Skipping...")
else:
    os.makedirs('./items')
    print("Created items folder!")

namespace_id = input("Type your namespace that you want to use. No quotes or spaces. \n\n> ")

list_input = input("\nType each file name with a space in between each name. Do not type .json after.\n\n> ")

formatted_list_input = list_input.replace(" ", ", ")

print("\nFiles to be created:")
print(formatted_list_input)

item_json_contents = {
    "format_version": "1.10",
    "minecraft:item": {
        "description": {
            "identifier": "minecraft_id:test",
            "category": "null"
        }
    }
}

watermark = "// This file was made by @MCGaming_Lukas. PLEASE DO NOT RE-DISTRIBUTE //\n"

ItemList = list_input.split()

formatted_json = json.dumps(item_json_contents, indent=2)

for names in ItemList:
    output_file = open('./items/%s.json' % names, 'w')
    print(watermark, file=output_file)
    replaced_json = formatted_json.replace("test", '%s' % names)
    print(replaced_json.replace("minecraft_id", namespace_id), file=output_file)
    output_file.close()

print("\nFiles created in the items folder in the current directory!")

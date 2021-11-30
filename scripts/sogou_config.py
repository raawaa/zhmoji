import json


def write_config(data: str, output: str):
    with open(data, "r", encoding="utf-8") as d:
        raw_data = json.load(d)
    with open(output, 'w', encoding="utf-8") as o:
        for k in raw_data:
            emojis = raw_data[k]
            for i in range(len(emojis)):
                o.write(f"{k},{i+3}={emojis[i]}\n")

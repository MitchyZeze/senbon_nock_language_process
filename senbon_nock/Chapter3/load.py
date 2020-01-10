import json

# .20〜.29で使用する関数
def load_json(country):

    with open("jawiki-country.json", "r") as jfile:
        for line in jfile:
            json_format = json.loads(line)
            if json_format["title"] == country:
                return json_format["text"]
    raise ValueError(f"{country}の記事はありません")

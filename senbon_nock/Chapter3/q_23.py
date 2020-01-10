# 23.セクション構造
# 記事中に含まれるセクション名とそのレベル(例えば"== セクション名 =="なら1）を表示せよ

# coding: utf-8

import re
import load

pattern = re.compile(r"""^(={2,})\s*(.+?)\s*\1.*$""", re.MULTILINE)

# 抽出
result = pattern.findall(load.load_json("イギリス"))

# 表示
# '==' => 1
for category in result:
    level = len(category[0]) - 1
    indent = "\t" * (level - 1)
    print(f"{indent}{category[1]}({level})")

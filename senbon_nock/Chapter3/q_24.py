# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルを抜き出す

# coding: utf-8

import re
import load

pattern = re.compile(r"""(?:ファイル|File):(.+?)\|""")

# 抽出
result = pattern.findall(load.load_json("イギリス"))

# 表示
for category in result:
    print(category)

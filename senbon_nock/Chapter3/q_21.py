# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ。

# coding: utf-8

import re
import load

# ex) [[Category:英連邦王国|*]]
# 正規表現 [[Category: で始まり (任意の文字列)　]] で終わる

pattern = re.compile(r"""^(.*\[\[Category:.*\]\].*)$""", re.MULTILINE)

# 抽出
result = pattern.findall(load.load_json("イギリス"))

# 表示
for category in result:
    print(category)

# 22. カテゴリの抽出
# 記事のカテゴリ名を(行単位ではなく名前で)抽出せよ

# coding: utf-8

import re
import load

# ex) [[Category:英連邦王国|*]]
# ex) [[Category:島国|くれいとふりてん]]
# 始めから]]か|が出てくるまでキャプチャ戦法
# [[Category: からキャプチャ対象

pattern = re.compile(r"""^.*\[\[Category:(.*?)(?:\]\]|\|).*$""", re.MULTILINE)

# 抽出
result = pattern.findall(load.load_json("イギリス"))

# 表示
for category in result:
    print(category)

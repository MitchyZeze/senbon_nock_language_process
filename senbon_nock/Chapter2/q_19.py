# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求めて、高い順に並べて表示せよ
# 確認にはcut,uniq,sortを用いること

# coding: utf-8

from itertools import groupby

filename = "hightemp.txt"

# １列目を抜き出しリストに格納
pres = [line.split("  ")[0] for line in open(filename).readlines()]
pres.sort()

# 都道府県で集計
result = [(pre, pres.count(pre)) for pre, counter in groupby(pres)]

# 出現頻度でソート
result.sort(key=lambda pre: pre[1], reverse=True)

# 表示
for ele in result:
    print(f" {ele[0]} {ele[1]}")

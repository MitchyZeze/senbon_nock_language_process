# 18.各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ(各行の内容は変更せずに並び変える)
# 確認にはsortコマンドを用いる。

# coding:utf-8

filename = "hightemp.txt"
lines = open(filename).readlines()
lines.sort(key=lambda line: float(line.split("  ")[2]))

for line in lines:
    print(line)

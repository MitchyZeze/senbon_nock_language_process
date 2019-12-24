# 14.先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り
# 入力のうち先頭のN行だけを表示せよ
# 確認にはheadコマンドを用いること

#coding :utf-8
import sys

filename = "hightemp.txt"
if not (int(sys.argv[1])) > 0:
    print("1以上の数を入力してください\n")
with open(filename) as file:
    for idx, line in enumerate(file):
        if idx >= int(sys.argv[1]):
            break
        print(line.rstrip())

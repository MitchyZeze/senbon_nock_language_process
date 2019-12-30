# 10.行数のカウント
# hightemp.txtを入力ファイルとして実行せよ。行数をカウントせよ。確認にはwcコマンドを用いよ

# coding: utf-8

filename = "hightemp.txt"
with open(filename) as lines:
    count = sum(1 for line in lines)
print(count)
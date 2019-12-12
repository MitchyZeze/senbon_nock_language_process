# .12 1列目をcol1.txtに2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに、2列目だけを抜き出したものをcol2.txtとして保存せよ。
# cut コマンドで確認せよ

# coding: utf-8

filename = "hightemp.txt"
with open(filename) as  data_file,  open('col1.txt', mode='w') as data_col1,  open('col2.txt', mode='w') as data_col2:
    for line in data_file:
        string = line.split('  ')
        data_col1.write(string[0] + '\n')
        data_col2.write(string[1] + '\n')
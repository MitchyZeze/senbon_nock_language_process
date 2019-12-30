# 13.col1.txtとcol2.txtのマージ
# 12で作った上記ファイル同士を結合し、元のファイルの1列目と2列目をタブ区切りで並べた
# テキストファイルを作成せよ。確認にはpasteコマンドを用いよ

with open('col1.txt') as col1_data, \
        open('col2.txt') as col2_data, \
        open('merge_col.txt', mode='w') as merge_file:
    for col1, col2 in zip(col1_data, col2_data):
        merge_file.write(col1.rstrip('\n') + '\t' + col2.rstrip('\n') + '\n')
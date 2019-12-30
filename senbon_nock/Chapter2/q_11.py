# 11.タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ。確認にはsed, tr, expandで試せ

# coding: utf-8

filename = "hightemp.txt"
with open(filename) as lines:
    for line in lines:
        print(line.replace('  ', ' '), end='')



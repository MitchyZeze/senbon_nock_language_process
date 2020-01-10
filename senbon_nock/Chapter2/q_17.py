# 17.1列目の文字列の異なり
# 1列目の文字列の種類(異なる文字列の集合)を求めよ。sort,uniqコマンドで確かめよ

#coding:utf-8

filename = "hightemp.txt"
with open(filename) as file:
    sets = set(line.split('  ')[0] for line in file)
for element in sets:
    print(element)
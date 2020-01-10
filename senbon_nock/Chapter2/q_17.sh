#!/bin/sh

# 1列目を切り出し、並び替えて重複行削除

cut -f 1 -d ' ' hightemp.txt | sort | uniq > q17_sort_col.txt

# スクリプトと実行との差分比較
python q_17.py | sort > q17sort_col_result.txt
diff -s  q17sort_col.txt  q17sort_col_result.txt
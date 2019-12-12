#!/bin/sh

# 12.py実行後に確認
# スクリプト実行とコマンド実行での生成ファイルの差分を確認する

cut -f 1 -d ' ' hightemp.txt > col1_test.txt
diff -s col1_test.txt col1.txt

cut -f 3 -d ' ' hightemp.txt > col2_test.txt
diff -s col2_test.txt col2.txt
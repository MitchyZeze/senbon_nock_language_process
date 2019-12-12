#!/bin/sh

# 13.py実行後に確認
# スクリプト実行とコマンド実行での生成ファイルの差分を確認する

paste col1.txt col2.txt > paste_col.txt
diff -s paste_col.txt merge_col.txt
#!/bin/sh

cut -f 1 -d ' ' hightemp.txt | sort | uniq -c | sort -r > q19_sort_col.txt
cat q19_sort_col.txt

# 20. JSONデータの読みこみ
# Wikipedia記事のJSONファイルを読みこみ「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

# coding: utf-8

import load

print(load.load_json("イギリス"))

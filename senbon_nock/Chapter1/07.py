# 07　テンプレートによる文生成　
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

def back_string(time, string1, string2):
    return (f"{time}時の{string1}は{string2}")

print(back_string(12, "気温", 22.4))
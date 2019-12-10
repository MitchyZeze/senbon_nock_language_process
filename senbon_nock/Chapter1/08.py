#08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# ・英小文字ならば(219 - 文字コード)の文字に置換
# ・その他の文字はそのまま出力

# この関数を用い，英語のメッセージを暗号化・復号化せよ．

import sys

def ciper(string):
    #result = ''
    #for char in string:
        # if char.islower():
        #     result += chr(219 - ord(char))
        # else:
        #     result += char
    result = ''.join(chr(219 - ord(char)) if char.islower() else char 
                for char in  string)
    return result

target = input("文字列を入力してください--> ")
result1 = ciper(target)
print(f"暗号化{result1}")

result2 = ciper(result1)
print(f"復号化{result2}")

if result1 != result2:
    sys.exit(1)

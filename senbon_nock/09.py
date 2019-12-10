# 09 Typoglycemia
# 間違っているのに読めてしまうという現象を指す。

# スペースで区切られた単語列に対して、各単語の先頭と末尾の文字は残し
# それ以外の文字の順序をランダムに並び替えるプログラムを作成する。
# ただし、長さが4以下の単語は並び替えないものとする。

import random

target_str = "I couldn`t believe that I could actually understand what I was reading : the phenomenal power of the human mind."
word_string = target_str.split(" ")
print(word_string)
result = []
for word in word_string:
    if len(word) <= 4:
        result.append(word)
    else:
        print("単語:{} 先頭文字:{} 末尾文字:{} シャッフル: {}".format(word, word[:1], word[-1:], ''.join(random.sample(word[1:-1], len(word[1:-1])))))
        result.append(word[:1] + ''.join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1:])
print(result)
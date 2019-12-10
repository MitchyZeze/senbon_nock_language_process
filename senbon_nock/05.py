# 05.n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．  
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ

def n_gram(target, num):
    result = []
    for i in range(0, len(target)- num+1):
        result.append(target[i:i + num])
    return result

target_string = "I am an NLPer"
target_words = target_string.split(' ')

result = n_gram(target_words, 2)
print(result)

result = n_gram(target_string, 2)
print(result)

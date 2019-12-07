## 03. 円周率
## "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ

string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
#print("string {}".format(string))
result = []
seperate_words = string.split(' ')
for seperate_word in seperate_words:
    #print("単語：{}".format(seperate_word))
    count = 0
    for char in seperate_word:
        if char.isalpha():
            count += 1
    result.append(count)

print("result: {}".format(result))

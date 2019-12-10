#"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."  
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，  
# それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）  
# への連想配列（辞書型もしくはマップ型）を作成せよ

target_string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
first_char = [1,5,6,7,8,9,15,16,19]
result = {}
words = target_string.split(" ")
print(words)

for (num, word) in enumerate(words, 1):
    if num in first_char:
        result[word[0:1]] = num
    else:
        result[word[0:2]] = num
print("result: {}".format(result))

# リスト操作版
#target_string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# str_count = [1,2,2,2,1,1,1,1,1,2,2,2,2,2,1,1,2,2,1]
# for i, (num, string) in enumerate(zip(str_count, target_string.split(' ')), 1):
#     print(i, string[0:num])



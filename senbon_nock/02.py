## パトカー」＋「タクシー」＝「パタトクカシーー」
## 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ

## リスト内包表記、zip、enumerate

for i, (str1, str2) in enumerate(zip([string1 for string1 in "パトカー"], [string2 for string2 in "タクシー"])):
    temp = str1 + str2
    if i == 0:
        result = ""
    result = result + temp
print(result)




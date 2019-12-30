# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

#coding:utf-8

import sys

def load(filename):
    if not (int(sys.argv[1])) > 0:
        print("1以上の数を入力してください")
        return False
    with open(filename) as file:
        lines = file.readlines()
        for line in lines[-int(sys.argv[1]):]:
    return True
    
def main():
    filename = "hightemp.txt"
    load(filename)
    
if __name__ == "__main__":
    main()
    
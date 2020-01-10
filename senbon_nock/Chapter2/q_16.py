# 16.ファイルをN分割する
# 自然数Nをコマンドライン引数などで受け取り
# 入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ

#coding:utf-8

import sys
import math

def load(filename):
    if not (int(sys.argv[1])) > 0:
        print("1以上の数を入力してね!!")
        return False
    with open(filename) as file:
        lines = file.readlines()
    
    rows = len(lines)
    split = math.ceil(rows/int(sys.argv[1]))

    for idx, row in enumerate(range(0, rows, split), 1):
        with open("16_{:02d}.txt".format(idx),"w") as temp_file:
            for line in lines[row:row + split]:
                temp_file.write(line)
    return True

def main():
    filename = "hightemp.txt"
    load(filename)

if __name__ == "__main__":
    main()


#06.集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，  
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．  
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．　

def n_gram(target, num):
    result = []
    for i in range(0, len(target)- num+1):
        result.append(target[i:i + num])
    return result


set_X = set(n_gram("paraparaparadise", 2))
set_Y = set(n_gram("paragraph", 2))

print("X: {}".format(set_X))
print("Y: {}".format(set_Y))

print("和集合 :{}".format(set_X|set_Y))
print("差集合 :{}".format(set_X-set_Y))
print("積集合 :{}".format(set_X&set_Y))

if "se" in set_X:
    print("seがXに含まれる")
elif "se" in set_Y:
    print("seがYに含まれる")
else:
    print("含まれない")

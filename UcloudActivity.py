# coding:utf-8
# 顺便问下你们还招人吗
import requests

__author__ = 'denonw'



def get_text():
    return requests.get("http://106.75.28.160/UCloud.txt").text


def count_ucanuup(txt):
    list = txt.split("UCanUup")
    return len(list) - 1


def count_by_index(txt):
    index = -1
    count = 0
    while True:
        try:
            index += 1
            index = txt.index("UCanUup", index)
            count += 1
        except:
            break
    return count

if __name__ == "__main__":
    txt = get_text()
    total = count_ucanuup(txt)
    total2 = count_by_index(txt)
    print(total)
    print(total2)
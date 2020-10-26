# https://www.acmicpc.net/problem/15904
import sys
input = sys.stdin.readline

word_list = list(input().split())

firsts = []
for i in word_list:
    firsts.append(i[0])

target = "UCPC"

result = []
for i in target:
    if i in firsts:
        result.append(firsts.index(i))
        del firsts[firsts.index(i)]

if len(result) < 4:
    print("I hate UCPC")
else:
    if result == sorted(result):
        print("I love UCPC")
    else:
        print("I hate UCPC")

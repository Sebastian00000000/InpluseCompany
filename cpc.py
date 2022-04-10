#!/bin/python3

import bots
cpc = bots.bot('cpc')
phrase = ['啊对对对', '桥洞底下盖小被']
for i in phrase:
    cpc.add_phrase(i)

print('秘制老八小汉堡，既美味又管饱')
talk = 10
while True:
    user_input = input()
    if user_input == 'exit':
        print("债见")
        break

    if talk <= 0:
        print('爷要猝死了，债见')
        break

    print(cpc.talk())
    if talk >= 10 and talk % 10 == 0:
        print(f'我还可以跟你聊{talk // 10}块钱的天')
    if talk < 10 and talk % 5 == 0:
        print(f'我还可以跟你聊{talk}毛钱')
    talk -= 1

import random


class Cpc:
    alias = '老八'
    def burgerKing(self):
        return "秘制老八小汉堡，既美味又管饱"
    def response(self):
        sentences = ['啊对对对', '桥洞底下盖小被']
        return sentences[random.randint(0,len(sentences) - 1)]

cpc = Cpc()

print(cpc.burgerKing())

talk = 10
while True:
    user_input = input()
    if user_input == 'exit':
        break
    elif talk == 0:
        print(f'我要猝死了，债见')
        break
    else:
        print(cpc.response())
        if talk >= 10 and talk % 10 == 0:
            print(f'我还可以跟你聊{int(talk / 10)}块钱的天')
        if talk < 10 and talk % 5 == 0:
            print(f'我还可以跟你聊{talk}毛钱')
        talk -= 1
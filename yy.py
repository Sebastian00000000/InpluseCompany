# #!/bin/bash
# import random


# msg_log = []
# msg_list = ['你职业厉害', '你装备好', 'T怎么拉的怪', '天赋点错了', '贵大网真的卡']
# msg = msg_list[random.randint(0, 4)]


# def saySomething():
#     global msg
#     if len(msg_log) > 3:
#         msg_log.pop(0)
#     while msg in msg_log:
#         msg = msg_list[random.randint(0, 4)]
#     else:
#         msg_log.append(msg)
#         return(msg)


# for i in range(0, 100):
#     print(saySomething())


import bots
yy = bots.bot('yy')
phrase = ['你职业厉害', '你装备好', 'T怎么拉的怪', '天赋点错了', '贵大网真的卡']
for i in phrase:
    yy.add_phrase(i)

msg_log = []
msg = yy.talk()
while True:
    while len(msg_log) > 3:
        msg_log.pop(0)

    while msg in msg_log:
        msg = yy.talk()

    user_input = input('')

    if user_input == 'exit':
        print("拜拜了您")
        break

    if user_input == '':
        print('哑巴？')
    else:
        msg_log.append(msg)
        print(msg)
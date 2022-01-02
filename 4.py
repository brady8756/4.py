# Tic Tac Toe
#井字遊戲、圈圈叉叉遊戲
import random

def 畫井字(格子):#劃出井字
    # 這個函式用來畫出井字

    # 格子是一個list存O或x或空的位子
    st.write('   |   |')
    st.write(' ' + 格子[7] + ' | ' + 格子[8] + ' | ' + 格子[9])#為格子編號
    st.write('   |   |')
    st.write('-----------')
    st.write('   |   |')
    st.write(' ' + 格子[4] + ' | ' + 格子[5] + ' | ' + 格子[6])
    st.write('   |   |')
    st.write('-----------')
    st.write('   |   |')
    st.write(' ' + 格子[1] + ' | ' + 格子[2] + ' | ' + 格子[3])
    st.write('   |   |')

def 決定符號():
    # 讓玩家選擇要O或X
    # 玩家的符號先放，電腦的放在後面
    符號 = ''
    while not (符號 == 'X' or 符號 == 'O'):#若輸入非O或X就在輸一次
        st.write('你要圈或是叉?(O/X)')
        符號 = input().upper()#將輸入轉成大寫

    # 第一個位子存玩家的符號，第二個存電腦的符號
    if 符號 == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def 誰先():#決定誰先
    # 亂數決定先後，若亂數是0就電腦先，若是1就玩家先
    if random.randint(0, 1) == 0:#做0或1的整數亂數
        return 'computer'
    else:
        return 'player'

def 在玩一次():
    # 若玩家想在玩一次就回傳true，若否就回傳false
    st.write('你想要在挑戰一次嗎? (yes 或 no)')
    return input().lower().startswith('y')#轉乘小寫，若是y就開始，只要不是y就結束遊戲

def 移動位子(格子, 符號, 位子):#控制要移動到哪裡
    格子[位子] = 符號

def 贏了(格子, 符號):
    # 給定格子和玩家使用的符號, 判斷玩家輸贏，若贏了了就回傳True
    return ((格子[7] == 符號 and 格子[8] == 符號 and 格子[9] == 符號) or # 最上面連成一條線
    (格子[4] == 符號 and 格子[5] == 符號 and 格子[6] == 符號) or #中間直行連成一條線
    (格子[1] == 符號 and 格子[2] == 符號 and 格子[3] == 符號) or #最下面連成一條線
    (格子[7] == 符號 and 格子[4] == 符號 and 格子[1] == 符號) or #最左側連成一條線
    (格子[8] == 符號 and 格子[5] == 符號 and 格子[2] == 符號) or #中間橫列連成一條線
    (格子[9] == 符號 and 格子[6] == 符號 and 格子[3] == 符號) or #最右側連成一條線
    (格子[7] == 符號 and 格子[5] == 符號 and 格子[3] == 符號) or #從左上到右下連線
    (格子[9] == 符號 and 格子[5] == 符號 and 格子[1] == 符號)) #從右上到左下連線

def 目前戰況(格子):
    # 複製目前的戰況.
    dupeBoard = []

    for i in 格子:
        dupeBoard.append(i)

    return dupeBoard

def 是否為空(格子, 位子):#判斷還有沒有未填入O或X的格子
    # 若還有位置就回傳True
    return 格子[位子] == ' '

def 玩家移動(格子):#讓玩家輸入要走的位子
    位子= ' '
    while 位子 not in '1 2 3 4 5 6 7 8 9'.split() or not 是否為空(格子, int(位子)):#若玩家輸入的數字不在1~9，或那一格不是空的，就重新輸入
        st.write('下一步要走哪? (1-9)')
        位子 = input()
    return int(位子)

def 見機移動(格子, 候選位子):
    #從候選位子選一個移動
    #回傳是否有空位
    可行位子 = []
    for i in 候選位子:
        if 是否為空(格子, i):
            可行位子.append(i)

    if len(可行位子) != 0:
        return random.choice(可行位子)
    else:
        return None

def 電腦移動(格子, 電腦符號):
    # 回傳電腦移動的位子
    if 電腦符號 == 'X':
        玩家符號 = 'O'
    else:
        玩家符號 = 'X'

    # 電腦移動到哪的判斷(AI)
    # 首先，找出可以贏的位子
    for i in range(1, 10):
        copy = 目前戰況(格子)
        if 是否為空(copy, i):
            移動位子(copy, 電腦符號, i)
            if 贏了(copy, 電腦符號):
                return i

    # 判斷玩家要贏的位子
    for i in range(1, 10):
        copy = 目前戰況(格子)
        if 是否為空(copy, i):
            移動位子(copy, 玩家符號, i)
            if 贏了(copy, 玩家符號):
                return i

    # 若四個角是空的，就選擇四個角走
    位子 = 見機移動(格子, [1, 3, 7, 9])
    if 位子 != None:
        return 位子

    # 若中間是空的就走中間
    if 是否為空(格子, 5):
        return 5

    # 移動到其他的空位
    return 見機移動(格子, [2, 4, 6, 8])

def 滿了(格子):
    # 若格子都滿了，就回傳True
    for i in range(1, 10):
        if 是否為空(格子, i):
            return False
    return True


st.write('開始玩井字遊戲')

while True:
  
    畫版 = [' '] * 10#重新產生一個空的井字
    玩家符號, 電腦符號 = 決定符號()#決定玩家和電腦是圈或是叉
    換誰 = 誰先()#從先的人開始
    st.write( 換誰 + '先')#輸出從誰開始
    遊戲進行中 = True#開始遊戲

    while 遊戲進行中:
        if 換誰 == 'player':#若現在是玩家走
            畫井字(畫版)#輸出井字
            位子 = 玩家移動(畫版)#畫版記錄位子
            移動位子(畫版, 玩家符號, 位子)

            if 贏了(畫版, 玩家符號):
                畫井字(畫版)
                st.write('哇嗚~你贏了!!')
                遊戲進行中 = False#結束遊戲
            else:
                if 滿了(畫版):#沒有空的格子
                    畫井字(畫版)
                    st.write('平手')
                    break
                else:#換電腦走
                    換誰 = 'computer'

        else:
            # 電腦走
            位子 = 電腦移動(畫版, 電腦符號)
            移動位子(畫版, 電腦符號, 位子)

            if 贏了(畫版, 電腦符號):
                畫井字(畫版)
                st.write('電腦獲勝，再接再厲吧~')
                遊戲進行中 = False#結束遊戲
            else:
                if 滿了(畫版):#沒有空的格子
                    畫井字(畫版)
                    st.write('平手')
                    break
                else:#換玩家走
                    換誰 = 'player'

    if not 在玩一次():
        break

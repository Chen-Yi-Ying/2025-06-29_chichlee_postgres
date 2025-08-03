import argparse
import random

def get_user_name()->str:
    """
    解析命令列參數以取得猜數字遊戲的使用者姓名。

    若未提供 '--name' 或 '-n' 參數，則會互動式要求使用者輸入姓名。
    同時接受可選的 '--frequency' 或 '-f' 參數以指定遊戲次數（預設為 1）。

    回傳:
        str: 使用者姓名，來源為命令列參數或使用者輸入。
    """
    parser = argparse.ArgumentParser(description="猜數字遊戲")
    parser.add_argument("-n","--name",type=str,help="姓名")
    parser.add_argument("-f","--frequency",type=int,help="玩的次數",default=1)
    args = parser.parse_args()

    if not args.name:
        name = input("請輸入您的姓名:")
    else:
        name = args.name

    return name

def play_game(name:str)->None:
    i = 0
    """
    猜數字遊戲函式。

    參數:
        name (str): 玩家名稱。

    功能說明:
        此函式會執行一個1到100之間的猜數字遊戲。玩家需在提示範圍內輸入數字，直到猜中隨機產生的目標數字為止。
        每次猜測後會提示玩家猜的次數及是否需要再大一點或再小一點，並在猜中後顯示總猜測次數。
    """
    print(f"========猜數字遊戲第{i+1}次=========\n\n")
    min = 1
    max = 100
    count = 0
    target = random.randint(min,max)
    print(target)
    while(True):
        keyin = int(input(f"猜數字範圍{min}~{max}:"))
        count += 1
        if(keyin>=min and keyin<=max):
            if target == keyin:
                print(f"賓果!猜對了, 答案是:{target}")
                print(f"{name}共猜了{count}次\n")
                break
            elif(keyin > target):
                print(f"猜錯了!再小一點")
                max = keyin - 1
            else:
                print(f"猜錯了!再大一點")
                min = keyin + 1
            print(f"{name}已經猜{count}次\n")
        else:
            print("請輸入提示範圍內的數字\n")

def main():
    """
    主函式，負責執行遊戲流程。
    1. 設定遊戲次數為 1。
    2. 取得使用者名稱。
    3. 執行遊戲指定次數。
    4. 結束後顯示使用者名稱及遊戲次數。
    """
    frequency = 1
    name = get_user_name()
    for i in range(frequency):
        play_game(name)
    print(f"遊戲結束,{name}共玩了{frequency}次")

if __name__ == '__main__':
    main()
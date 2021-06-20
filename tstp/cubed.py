import math

def cal():
    while True:
        num = input("数字を入力してください（終了したい場合はq）")

        if num == "q":
            break
        
        try:
            num = int(num)
        except ValueError:
            print("文字は入力できません")
            continue

        cal_num = math.pow(num, 3)

        print(cal_num)
left_coffee = 10
money=0
while True:
    money = money + int(input("돈을 넣어주세요"))
    while money:
        print("커피 나왔습니다.")
        money-=300
        left_coffee -=1
        if money<300:
            print(f"잔액은 {money}원입니다.")
            break
            
    
    
    if left_coffee <= 0:
        print("커피가 떨어졌습니다.")
        break
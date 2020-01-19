import os

while(1):
    
    try:
        s = int(input("수입력:"))
    except:
        os.system("cls")
        print("다시 입력해주세요.")
        
    else:
        print(s, "okay")
        break

str(input())

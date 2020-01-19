#test3.py
print("Start")

list1 = [100, 200, 300]

def getitem(idx):
    return list1[idx]

try:
    for i in range(4):
            print(getitem(i))

except IndexError:
    print("abnormal" "IndexError")
else:
    print("normally execute")

finally:
    print("finally block execute")

print("End")

str(input())
    

    
#python test3.py로 실행합니다.

#예외 처리해주세요....

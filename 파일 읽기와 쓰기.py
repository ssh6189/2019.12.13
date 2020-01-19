파일의 개념
파일은 컴퓨터를 실행할 때 가장 기본이 되는 단위

파일의 종류
바이너리파일 : 컴퓨터만 이해할 수 있는 이진법 형식으로 저장된 파일
일반적으로 메모장으로 열면 내용이 깨져보임
ex)엑셀, 워드

텍스트파일 : 사람도 이해할 수 있는 문자열 형식으로 저장된 파일
메모장으로 열면 내용확인이 가능
메모장에 저장된 파일, HTML 파일, 파이썬 코드 파일 등

파일 읽기

f = open("디렉토리 및 파일명", "열기모드")
r : 읽기모드
w : 쓰기모드
a : 파일의 마지막의 새로운 내용을 추가할때

append를 안쓰면 덮어쓰기가 된다.

text파일은 내부적으로포인터가 있다.

f = open("dream.txt", "r")
contents = f.read()
print(contents)
f.close()

with문과 함께 사요하기

with문과 함께 open()함수를 사용할 수 있다. with문은 들여쓰기를 사용해 들였쓰기가
있는 코드에서는 open()함수가 유지되고, 들여쓰기가 종료되면 open()함수도 끝나는
방식이다.
close가 없어도, with가 끝나면 자동으로 닫힌다.

with open("dream.txt", "r") as my_file:
    contents = my_ile.read()
    print(type(contents), contents)

한줄씩 읽기
readlines() 함수를 사용하여 한줄씩 내용을 읽어 문자열 형태로 저장할 수 있다.

with open("dream.txt", "r") as my_file:
    contents = my_file.readlines()
    print(type(content_list))
    print(content_list)

readline()함수는 실행할 때마다 차례대로 한줄씩 읽어오는 함수이다.

with open("dream.txt", "r") as my_file:
    i = 0
    while 1:
        line = my_file.readline()
        if not Line:
            break
        print(str(i)+"==="+line.replace("\n",""))
        i = i + 1

파일 읽기 : 파일 안 글자의 통계정보 출력하기
때로는 파일 안 텍스트의 통계정보를 읽어와야 할때가 있다. 이를 위해 많이 사용하는
방법은 이미 배운 split() 함수와 len()함수를 함께 사용하는 것이다.

with open("dream.txt", "r") as my_file:
          contents = my_file.read()
          word_list = contents.split(" ")
          line_list = contents.split("\n")

print("총 글자의 수 :". len(contents))
print("총 단어의 수 :". len(word_list))
print("총 줄의 수 :". len(line_list))



파일 쓰기 : 텍스트 파일을 저장하기 위해서는 텍스트 파일을 저장할 때 사용하는 표준을
지정해야 하는데, 이것을 인코딩이라고 한다.

f.write("들어갈내용")

f = open("count_log.txt", 'w', encoding = "utf8")
for i in range(1, 11):
    data = "%d번째 줄이다. \n"%i
    f.write(data)

f.close()

실행을 하면, 덮어쓰기가 된다.


with open("count_log.txt", 'a', encoding = "utf8") as f:
    for i in range(1, 11):
        data = "%d번째 줄이다. \n"%i
        f.write(data)

파일 쓰기 : 파일 열기모드 a로 새로운 글 추가하기
상황에 따라 파일을 계속 추가해야하는 작업이 있을 수도 있으므로, 기존 파일에
추가 작업을 해야하는 일이 있다. 이 경우, 많이 사용하는 방법은 추가 모드 a를 사용하는것이다.


파일 쓰기 : 디렉토리 만들기

파이썬으로는 파일만 다루는것이 아니라, 디렉토리도 함께 다를 수 있다. os모듈을 사용하면
디렉터리를 쉽게 만들 수 있다.

os.mkdir : 폴더 생성
os.path.isdir : 기존 디렉토리 존재여부 확인
so.chdir("dir path")는 현재 디렉토리의 위치를 변경
os.getcwd()는 현재 작업디렉토리 확인
os.listdir("path")는 인수 path 경로 아래 파일이나 디렉토리 리스트 반환
os.path.exist("path")파일 또는 디렉토리 경로가 존재하는지 체크
os.path.isDir()
os.path.isFile()
os.path.getsize("file path")파일 크기 알려줌
os.rmdir("dir name")디렉토리 삭제
os.rename(old, new)파일 이름 변경
os.system("cls") 시스템에서 제공해주는 (운영체제)의 명령어, 프로그램을 호출
os.unlink("file path") 파일삭제
os.stat는 파일 정보를 반환
#요정도는 기억해두면 여러 상황에서 유용하게 사용할 수 있다.

import os
print(os.getcwd())
os.chdir("c:/Temp")
print(os.getcwd())
os.chdir("c:/worksapace")
os.listdir("C:/workspace")



파일 쓰기 : 로그파일 만들기
로그파일은 프로그램이 동작하는동안 여러가지 중간기록을 하는 파일이다.



pickle 모듈
파이썬은 pickle 모듈을 제공하여, 메모리에 로딩된 객체를 영속호할 수 있도록 지원한다.

pickle 모듈을 사용하기 위해서는 다음과 같이 호출한 후 객체를 저장할 수 있는 파일을
열고 저장하고자 하는 객체를 넘기면(dump)된다. 파일을 생성할 때는 w가 아닌
wb로 열어야 하는데, 여기서 b는 바이너리(binary)를 뜻하는 약자로, 텍스트파일이 아닌
바이너리 파일이 저장된것을 확인할 수 있다. dump()함수에서는 저장할 객체, 저장될 파일객체를
차례대로 인수로 넣으면 해당 객체가 해당 파일에 저장된다.

저장된 pickle파일을 불러오는 프로세스도 저장 프로세스와 같다. 먼저 list.picle 파일을
rb모드로 읽어 온 후, 해당 파일 객체를 pickle 모듈을 사용하여, load() 함수를 불러오면
된다. 다음 파이썬 셀코드는 앞에서 리스트 객체를 list.pickle 파일에 저장했기 때문에 해당
파일을 불러 사용할 때도 동일하게 리스트 객체가 반환된것을 확인할 수 있다.

import pickle

f = open("list.pickle", "wb")
test = [1, 2, 3, 4, 5]
pickle.dump(test, f)
f.close()

f = open("list.pickle", "rb")
test_pickle = pickle.load(f)
print(test_pickle)
f.close()


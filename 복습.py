객체지향 특성 - 상속, 다형성, 캡슐화
########
객체(object) - 실체(사물, 개념)
클래스 : 객체를 생성하기 위한 설계도, data+기능(동작), C언어의 구조체 + 함수
장점 : 필요한 속성과 메서드를 사용자가 정의하여 사용가능
인스턴스화, 인스턴스

class 클래스이름[(부모클래스)] : #상속받을 부모클래스가 생략된것
    #생략시 파이썬의 최상위 클래스인 object 상속을 받는다.

    클래스 소유의 변수 선언가능
    클래스 변수....

    def __init__(self, 인수1, 인수2):
        self.인스턴스변수 = 인수1
        

    def 클래스 함수(self, 인수1, 인수2):
        수행문장1
        ....

    def __str__(self):#출력함수
        표현할 문자열
        #객체를 표현할 문장 리턴

객체생성

객체 = 클래스이름(인수1, 인수2, 인수....) #클래스에 정의된 init메서드의 인수에 맞춰서
#객체생성을 해야한다.

#type이라는 메타클래스가 인스턴스 생성

__new__() -> __init__()를 호출해서 메모리에 인스턴스를 형성


먄약, 다음과 같은 메서드의 기능이 있는 클래스가 있다.
               객체를 생성할때마다, 메모리에 생성하는것보다
               클래스에 메서드를 정의해놓고 인스턴스가 사용할때마다
               가져와서 실행하는것이 더 낫다.

객체.메서드(인수1, 인수2, 인수....)
#메서드의 self 인수를 제외한 인수에 맞춰서 호출

객체가 메모리에서 제거될 때 수행해야할 작업이 있다면, 클래스에 __del__이라고 하는
(self):재정의(오버라이트해서) 구현합니다.

static 메서드라고 하는게 있다.
클래스로부터 객체를 생성없이 클래스 이름으로 호출해서 사용하면 된다.
static 메서드는 메서드 선언앞에 @staticmethod 데코레이션을 선언하고 메서드의 첫번째 인수로 self를
선언하지 않는다.


class Calculator:
    @:staticmethod : 데코레이션
    def plus(a, b):
        return a + b

if __name__ =='__main__': #만약, 모듈이름이 메인이면 다음을 실행
    print(Calculator.plus(10,20))



클래스 변수에 접근하는 변수는 클래스 메서드를 만들어야한다.
@class method를 메서드 앞에 데코레이터로 선언을 해야한다.
클래스 자신을 메서드의 첫번째 인수로 전달해야 하므로 메서드 인수의 첫 인수로, cls를 선언합니다.

class InstanceCounter:
    count = 0
    def __init__(self):
        InstanceCounter.count = count + 1

    @classmethod
    def print_instance_count(cls):
        print("생성된 인스턴스 개수는 : ", cls.count)

if __name__ == '__main__':
    x1 = InstanceCounter()
    InstanceCounter.print_instance_count()

    x2 = InstanceCounter()
    InstanceCounter.print_instance_count()

    x3 = InstanceCounter()
    InstanceCounter.print_instance_count()



#인스턴스만 접근 할 수 있는 속성을 선언하려면
    (private 변수를 선언하려면)

class HasPrivate:
    def __init__(self):
        self.public = "public"
        self.__private = "private"

    def print_internal(self):
        print(self.public) #인스턴스 내부에서는 접근 가능
        print(self.__private) #인스턴스 내부에서는 접근 가능

object1 = HasPrivate()
object1.print_internal()
print(object1.public)
print(object1.__private) #인스턴스 외부에서는 접근 불가

#private 인스턴스 속성을 생성된 객체로부터 외부에서 접근하려면 setter/getter메서드를 만들어
주어야 합니다.

#getter 메서드는  @property 데코레이터 선언
#setter 메서드는 @name.setter 데코레이터 선언

class HasPrivate:
    def __init__(self, input1, input2):
        self.public = input1
        self.__private = input2

    def print_internal(self):
        print(self.public) #인스턴스 내부에서는 접근 가능
        print(self.__private) #인스턴스 내부에서는 접근 가능

    @property
    def getPrivate(self):
        return self.__private

    @private.setter #메서드명.setter 데코레이션 선
    def setPrivate(self, input_private):
        self.private = input_private

object1 = HasPrivate()
object1.print_internal()
print(object1.__private)
print(object1.getPrivate())
object1.setPrivate("indirect")
print(object1.getPrivate())



어제

class Person:
    pass
class Student(Person):
    pass

print(issubclass(자식클래스, 부모클래스))#상속관계 확인

#파이썬은 다중상속 허용한다.
class Lion:
    def Jump(self):
        print("호랑이보다 점프 실력 낮음")

class Tiger:
    def Bite(self):
        print("사자보다 강함")

class Liger(Tiger, Lion):
    def play(self):
        print("사자보다 강할까요? 호랑이보다 강할까요?")

#자식클래스에서 부모클래스로부터 상속받은 메소드를 재정의할 수 있다.
#재정의한 자신의 메서드 대신 부모로부터 상속받은 메서드를 명시적으로 호출하고 싶으면
super().메서드()

가장 앞에 있는것을 결과 나온다.
Quiz1
class A:
    def method(self):
       print("A")

class B:
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

class D(B, C):
    pass

class E(C, B):
    pass

obj1 = D()
obj1.method()

obj2 = E()
obj2.method()

Quiz2
클래스는 동일한 기능을 수행하지만, 속성이 다른 여러 객체를 사용해야할 경우 클래스로 정의합니다.
하나의 기능을 수행한다면, 기능만 정의해주면 된다. 즉, 모듈로 만들어서 재사용한다.(실행시에 복사본은 하나만 사용한다.)

연관된 모듈을 그룹할 수 있다. - 패키지
모듈은 물리적으로 하나의 파이썬 스크립트 파일 .py
패키지는 물리적으로 디렉토리다.
패키지 내부에도 서브 패키지를 정의할 수 있다.
패키지를 구성할때 필수 파일 : __init__.py(패키지 내부의 서브 패키지 구성정보, 모듈 구성정보)를 구성한다.

#모듈 사용하기
#작업 디렉토리에 사용할 패키지와 모듈이 구성되어 있어야 합니다.
#from 패키지.모듈 import ((변수, 함수, 클래스)등의 속성)
함수
변수
객체 = 클래스()

from 패키지 import 모듈
모듈.함수
모듈.변수

from 패키지 import 모듈 as 별칭
별칭.함수
별칭.변수

모듈은 계층구조로 호출되어 사용될 수 있다.
최상위 (Top level)에서 실행되는 파이썬 스크립터(모듈)
내장 전역변수 __name__에 모듈이름대신 __main__이 지정된다.



예외(exception):가벼운 오류, 논리적 오류로써, 예외가 발생하면,
프로그램은 실행이 종료됩니다.

예외처리를 통해서 프로그램이 예외가 발생되더라도 종료되지 않고 계속 다음 실행으로
제어할 수 있도록 할 수 있습니다.

a = [100, 200, 300]
print(a[3])

-내장된 예외-
index error
name error
zerodivision error
type error
attribure error

내장된 예외 클래스들은 전부 exceptions 모듈에 미리 정의되어 있습니다.
사용자 정의 예외 클래스를 정의해서 사용할 수 있습니다. (Exception-BaseException 예외 클래스를 상속받아서 만들면 된다.)

예외 발생 가능성이 있는 문장

try:
    예외 발생 가능성이 있는 문장
    문장#수행 안함

except 예외 타입 as 별칭:
    예외처리 문장

except 예외 타입 as 별칭:
    예외처리 문장
    .
    .
    .
    .

else:
    #예외가 발생하지 않았을때만 수행할 문장

finally:
    #예외 발생 유무와 상관없이 수행할 문장

다음 실행 문장


#test3.py
print("Start")


list1 = [100, 200, 300]

def getitem(idx):
    return list1[idx]

print("End")

print(getitem(0))
print(getitem(3))

#python test3.py로 실행합니다.

#예외 처리해주세요....
다음실행문장

예외 발생 유무와 상관없이 수행할 문장은 "finally block execute"
예외가 발생하지 않은 경우 수행할 문장은 "nomally execute"
예외가 발생한 경우 발생한 예외타입 이름과 "abnormal"


except는 여러개 사용가능



예외 발생시킬때 raise
수행처리전에 조건을 체크해서 조건을 만족하지 않을때 예외발생 assert

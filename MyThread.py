from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import GamePage
import time
import sys


# https://wikidocs.net/1744 - 시그널 슬롯 설명 블로그  

class MyThread(threading.Thread, QtCore.QObject):
    resultSignal = QtCore.pyqtSignal(str)   # - 네임스페이스 전역변수로 침
    # 파일.변수로 해도 값을 가져올 수 있기 때문에 편함. -> 객체로 선언받을때가 아닌 파일을 객체로 선언한뒤 데이터를 가져올 수 있음.
    # ex) 
    # self.myThread = MyThread.MyThread()
    # self.myThread.resultSignal이 작동한다

    # 마이쓰레드가 기준이 아니라 이 파일단위로 만들어질 수 있따. 
    # PyQt는 위젯에 정의된 이벤트를 시그널(signal)이라고 부르고 이벤트가 발생할 때 호출되는 함수나 메서드를 슬롯(slot)이라고 부릅니다.
    # 또한 자신의 시그널을 정의하려면 클래스 변수로 정의해야합니다.
    # 쓰레드 클래스가 두개 이상 클래스에 쓰이면 클래스를 만들고 하나에만 쓰이면 게임페이지에 한 파일로 만들기
    # FEEDBACK: 쓰레드를 통한 결과값을 받는 방법 중 1개 ( Signal/Slot )
    # FEEDBACK: 클래스 안에서 사용하는 전역변수 즉, 멤버변수와 동일하지만 이렇게 적어주어야만 함

    def __init__(self, revui):
        threading.Thread.__init__(self)
        QtCore.QObject.__init__(self)  #QtCore.QObject 안의 생성자 함수를 강제로 실행시켜주는 코드 
        self.ui = revui # - 인스턴스 네임스페이스
        # self.num = 0
        self.gameList = ["가위","바위","보"]
        self.locale = 0
    #쓰레드안에서는 GUI작업을 해주면 안된다.
    #위에는 self.num = 0일때 계속 돌고

    def run(self):          
        while True:         
            print("1")
            print("2")
            print("3")
            # 시그널
            self.resultSignal.emit(self.gameList[self.locale])  
            self.locale += 1
            self.locale %= 3
            time.sleep(1)

    # FEEDBACK: 알고리즘적으로 최적화 되어있음
    # FEEDBACK: emit을 통해 slot으로 데이터를 보내줄 수 있음. 보내주는 데이터는 emit 괄호 안에 들어가는 데이터


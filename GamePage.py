from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
import random
import MyThread

class GamePage:
    def __init__(self, revui):
        self.ui = revui
        self.init_event()
        
        a = MyThread.resultSignal
    def init_event(self):
        self.myThread = MyThread.MyThread(self.ui)
        self.myThread.resultSignal.connect(self.resultChange)   # FEEDBACK: 쓰레드 클래스 안에 있는 Signal과 여기 페이지에서 만든 slot을 연결하는 과정
        self.myThread.start()

    # 슬롯
    def resultChange(self, value):
        self.ui.result[0].setText(value)
        self.ui.result[0].setAlignment(QtCore.Qt.AlignCenter)
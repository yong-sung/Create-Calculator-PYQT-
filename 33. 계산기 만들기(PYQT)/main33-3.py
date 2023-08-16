import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic


ui_path = r"33. 계산기 만들기(PYQT)\계산기.ui"
form_class = uic.loadUiType(ui_path)[0] # UI 파일을 로드해 해당 UI에 대한 클래스를 가져와 'form_class' 변수에 할당


class WindowClass(QMainWindow, form_class) : # 'QMainWindow' 클래스와 UI 파일에서 생성된 클래스를 상속받아 새로운 클래스 정의
    def __init__(self) :
        super().__init__()
        self.setupUi(self) # UI 요소를 초기화
        
        # 버튼들을 클릭 이벤트와 'btn_clicked' 메서드를 연결. 각 버튼이 클릭됐을 때 'btn_clicked' 메서드 호출됨
        self.btn_C.clicked.connect(self.btn_clicked)
        self.btn_number0.clicked.connect(self.btn_clicked)
        self.btn_number1.clicked.connect(self.btn_clicked)
        self.btn_number2.clicked.connect(self.btn_clicked)
        self.btn_number3.clicked.connect(self.btn_clicked)
        self.btn_number4.clicked.connect(self.btn_clicked)
        self.btn_number5.clicked.connect(self.btn_clicked)
        self.btn_number6.clicked.connect(self.btn_clicked)
        self.btn_number7.clicked.connect(self.btn_clicked)
        self.btn_number8.clicked.connect(self.btn_clicked)
        self.btn_number9.clicked.connect(self.btn_clicked)
        self.btn_result.clicked.connect(self.btn_clicked)
        self.btn_minus.clicked.connect(self.btn_clicked)
        self.btn_add.clicked.connect(self.btn_clicked)
        self.btn_multipy.clicked.connect(self.btn_clicked)
        self.btn_divide.clicked.connect(self.btn_clicked)

        self.le_view.setEnabled(False)
        
        self.text_value = ""
    
    # 버튼 클릭 이벤트를 처리. 클릭된 버튼의 텍스트 값을 가져와서 해당 값에 따라 다양한 동작을 수행    
    def btn_clicked(self):
        btn_value = self.sender().text()
        if btn_value == 'C':
            print("clear")
            self.le_view.setText("0")
            self.text_value = ""
        elif btn_value == '=':
            print("=")
            try:
                
                # 시작 부분에 있는 0을 제거하기 위해 사용 
                resultValue = eval(self.text_value.lstrip("0")) # Ex) eval("0123+456") -> eval("123+456") 
                
                # 계산 결과인 'resultValue' 를 문자열로 변한한 뒤, 'le_view' 라는 이름의 QLineEdit 위젯에 표시
                self.le_view.setText(str(resultValue))
            except: # 'eval()' 함수가 예외를 발생시키면 실행
                self.le_view.setText("error")
        else:
            if btn_value == 'X':
                btn_value = '*'
            self.text_value = self.text_value + btn_value
            print(self.text_value)
            self.le_view.setText(self.text_value)

# 프로그램이 직접 실행될 때만 'app' 객체를 생성하고 'WindowClass' 객체를 생성해 애플리케이션을 실행
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec_() #PyQt5 애플리케이션의 메인 루프를 실행, 사용자 인터페이스의 상호작용을 처리
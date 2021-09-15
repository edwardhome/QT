from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox

def handleCalc():
    info1 = textEdit.toPlainText()
    info2 = textEdit_1.toPlainText()
    QMessageBox.about(window,"彈跳視窗",f"輸出結果 {info1}\n {info2}")

def clear():
    textEdit.clear()
    textEdit_1.clear()

app = QApplication([]) #建立應用程式
window = QMainWindow() #建立視窗物件
window.resize(500,240) #確定視窗大小
window.move(810,340) #開啟左上角在螢幕的位置
window.setWindowTitle("圖形化程式") 

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("預設輸入文字")
textEdit.move(10,10)
textEdit.resize(300,100)

textEdit_1 = QPlainTextEdit(window)
textEdit_1.setPlaceholderText("預設輸入文字")
textEdit_1.move(10,120)
textEdit_1.resize(300,100)

button = QPushButton("合計",window)
button.move(380,10)
button.resize(100,100)
button.clicked.connect(handleCalc)

button_1 = QPushButton("清除",window)
button_1.move(380,120)
button_1.resize(100,100)
button_1.clicked.connect(clear)


window.show()
app.exec() #執行該程式的事件處理循環


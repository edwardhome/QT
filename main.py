from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox

def handleCalc():
    info = textEdit.toPlainText()
    QMessageBox.about(window,"彈跳視窗",f"測試結果={info}")

app = QApplication([]) #建立應用程式
window = QMainWindow() #建立視窗物件
window.resize(500,400) #確定視窗大小
window.move(810,340) #開啟左上角在螢幕的位置
window.setWindowTitle("圖形化程式") 

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("預設輸入文字")
textEdit.move(10,10)
textEdit.resize(300,380)

button = QPushButton("合計",window)
button.move(380,80)
button.resize(100,100)
button.clicked.connect(handleCalc)

window.show()
app.exec() #執行該程式的事件處理循環


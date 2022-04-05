if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QFrame

def buildQHBoxLayout(target, widgets):
    '''Build a horizontal layout box'''
    layout = QHBoxLayout()
    for widget in widgets:
        layout.addWidget(widget)
    target.setLayout(layout)

def buildQVBoxLayout(target, widgets):
    '''Build a vertical layout box'''
    layout = QVBoxLayout()
    for widget in widgets:
        layout.addWidget(widget)
    target.setLayout(layout)

class Button(QPushButton):
    def __init__(self, name):
        super().__init__(name)
        self.setStyleSheet("""
            Button {
                width: 200px;
                height: 30px;
                background-color: #222222;
                border: 3px solid DimGray;
                border-radius: 5px;
                color: DimGray;
                font: bold 14px;
            }
            Button:focus {
                border-color: DarkOliveGreen;
                color: DarkOliveGreen;
            }
            Button:hover {
                background-color: #333333;
            }
            Button:pressed {
                background-color: DarkOliveGreen;
                color: #222222;
            }
            """)

class FrameContent(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            FrameContent {
                background-color: #111111;
                min-width: 500px;
                min-height: 500px;
            }
            """)

class FrameMenu(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            FrameMenu {
                background-color: #222222;
                max-width: 210px;
                min-width: 210px;
            }
            """)
        testButton1 = Button('Test Button 1')
        testButton2 = Button('Test Button 2')
        testButton3 = Button('Test Button 3')
        buildQVBoxLayout(self, [testButton1, testButton2, testButton3])

class FrameFoot(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            FrameFoot {
                background-color: #000000;
                max-height: 20px;
                min-height: 20px;
            }
            """)

class FrameBody(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            FrameBody {
                background-color: #ffffff;
            }
            """)
        frameMenu = FrameMenu()
        frameContent = FrameContent()
        buildQHBoxLayout(self, [frameMenu, frameContent])

class FrameHead(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            FrameHead {
                background-color: #000000;
                max-height: 30px;
                min-height: 30px;
            }
            """)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MIR4 - Clan Manager')
        self.resize(1024, 720)
        self.version = 'alpha 0.1.0'
        self.colors = ['#222222', 'DimGray', 'DarkOliveGreen']
        self.setStyleSheet("""
            MainWindow {
                background-color: #111111;
                margin: 0;
                padding: 0;
                border: 0;
            }
            """)
        self.clans = []
        self.setProperty('topMargin', 0)

        frameHead = FrameHead()
        frameBody = FrameBody()
        frameFoot = FrameFoot()
        buildQVBoxLayout(self, [frameHead, frameBody, frameFoot])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

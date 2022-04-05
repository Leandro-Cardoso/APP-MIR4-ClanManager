if __name__ == '__main__':
    from PyQt5.QtWidgets import QFrame

class FrameAddClan(QFrame):
    '''Add a new Clan object'''
    pass

class FrameClan(QFrame):
    '''Show a Clan object'''
    pass

class FrameClanSelection(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            FrameClanSelection {
                background-color: #111111;
                min-width: 500px;
                min-height: 500px;
            }
            """)

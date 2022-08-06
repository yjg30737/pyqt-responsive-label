from PyQt5.QtWidgets import QLabel, QSizePolicy, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class ResponsiveLabel(QLabel):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__parent = parent
        if self.__parent:
            self.__parent.installEventFilter(self)
        self.installEventFilter(self)

        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__text_change_flag = False

    def __initUi(self):
        self.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.setMinimumSize(self.sizeHint())

    def __setApproximateFontSize(self):
        dpr = QApplication.screens()[0].logicalDotsPerInch() / 96.0
        self.setFont(QFont('Arial', max(12, min(self.widthMM()//2, self.height()-2) // dpr)))

    def __setFontSizeAccordanceWithWindow(self):
        # Set the label font size accordance with windows size "approximately"
        self.__setApproximateFontSize()

    def setAcceptTextChange(self, f: bool):
        self.__text_change_flag = f

    def eventFilter(self, obj, e):
        # accept window's resize event
        if isinstance(obj, type(self.__parent)):
            if e.type() == 14:
                self.__setFontSizeAccordanceWithWindow()
        # accept text changing event
        if self.__text_change_flag:
            if isinstance(obj, ResponsiveLabel):
                if e.type() == 12:
                    self.__setFontSizeAccordanceWithWindow()
        return super().eventFilter(obj, e)

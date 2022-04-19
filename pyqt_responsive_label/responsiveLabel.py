from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class ResponsiveLabel(QLabel):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__parent = parent
        if self.__parent:
            self.__parent.installEventFilter(self)

        self.installEventFilter(self)
        self.__initUi()

    def __initUi(self):
        self.setAlignment(Qt.AlignCenter)

    def __setFontSizeAccordanceWithWindow(self):
        dpr = self.devicePixelRatio()
        self.setFont(QFont('Arial', min(200 // dpr, max(10, self.widthMM() // dpr))))
        # todo generalize, not brute force (if possible)
        # self.setFont(QFont('Arial', min(200 // dpr, max(10, math.floor(self.widthMM() // dpr * self.width() / self.fontMetrics().boundingRect(self.text()).width())))))

        while self.width() / self.fontMetrics().boundingRect(self.text()).width() <= 1.0:
            font = self.font()
            font.setPointSize(font.pointSize()-1)
            self.setFont(font)

        while self.height() / self.fontMetrics().boundingRect(self.text()).height() <= 0.7:
            font = self.font()
            font.setPointSize(font.pointSize()-1)
            self.setFont(font)

    def eventFilter(self, obj, e):
        if isinstance(obj, type(self.__parent)):
            if e.type() == 14:
                self.__setFontSizeAccordanceWithWindow()
        elif isinstance(obj, ResponsiveLabel):
            if e.type() == 12:
                self.__setFontSizeAccordanceWithWindow()
        return super().eventFilter(obj, e)

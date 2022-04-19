import math

from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class ResponsiveLabel(QLabel):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__parent = parent
        self.__parent.installEventFilter(self)
        self.installEventFilter(self)
        self.__initUi()

    def __initUi(self):
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

    def __setFontSizeAccordanceWithWindow(self):
        dpr = self.devicePixelRatio()
        self.setFont(QFont('Arial', min(200 // dpr, max(10, self.widthMM() // dpr))))
        self.setFont(QFont('Arial', min(200 // dpr, max(10, math.floor(
            self.widthMM() // dpr * self.width() / self.fontMetrics().boundingRect(self.text()).width())))))

    def eventFilter(self, obj, e):
        if isinstance(obj, type(self.__parent)):
            if e.type() == 14:
                self.__setFontSizeAccordanceWithWindow()
        elif isinstance(obj, ResponsiveLabel):
            if e.type() == 12:
                self.__setFontSizeAccordanceWithWindow()
        return super().eventFilter(obj, e)

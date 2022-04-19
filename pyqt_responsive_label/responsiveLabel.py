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
        self.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

    def __setApproximateFontSize(self):
        dpr = self.devicePixelRatio()
        self.setFont(QFont('Arial', min(200 // dpr, max(10, self.widthMM() // dpr))))

    def __setAccurateFontWidth(self):
        while self.width() / self.fontMetrics().boundingRect(self.text()).width() <= 1.0:
            font = self.font()
            font.setPointSize(font.pointSize() - 1)
            self.setFont(font)

    def __setAccurateFontHeight(self):
        font_size = min(self.height(), self.fontMetrics().boundingRect(self.text()).height())
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def __setFontSizeAccordanceWithWindow(self):
        # Set the label font size accordance with windows size "approximately"
        self.__setApproximateFontSize()

        # Set the label font size accordance with windows size "accurately"

        # todo generalize, not brute force (if possible)
        # self.setFont(QFont('Arial', min(200 // dpr, max(10, math.floor(self.widthMM() // dpr * self.width() / self.fontMetrics().boundingRect(self.text()).width())))))

        # Set the label font size smaller than affordable width
        self.__setAccurateFontWidth()
        # Set the label font size smaller than affordable height
        self.__setAccurateFontHeight()

    def eventFilter(self, obj, e):
        # accept window's resize event
        if isinstance(obj, type(self.__parent)):
            if e.type() == 14:
                self.__setFontSizeAccordanceWithWindow()
        # accept text changing event
        elif isinstance(obj, ResponsiveLabel):
            if e.type() == 12:
                self.__setFontSizeAccordanceWithWindow()
        return super().eventFilter(obj, e)

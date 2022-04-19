# pyqt-responsive-label
PyQt QLabel which can resize the font responsively accordance with window's size change

## Requirements
* PyQt5 >= 5.8

## Setup
`pip3 install git+https://github.com/yjg30737/pyqt-responsive-label.git --upgrade`

## Example
```python
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from pyqt_responsive_label import ResponsiveLabel


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        responsiveLabel = ResponsiveLabel(self)
        responsiveLabel.setText('ABC')

        lay = QVBoxLayout()
        lay.addWidget(responsiveLabel)

        self.setMinimumSize(responsiveLabel.sizeHint())
        self.setLayout(lay)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    app.exec_()
```

Result

Like below, label font size is changing accordance with window's size.

![image](https://user-images.githubusercontent.com/55078043/163919017-31d6ae6b-329a-414e-ad37-a09dee778faf.png)

![image](https://user-images.githubusercontent.com/55078043/163919028-c718a549-71bf-4581-8f28-19c6a36719fc.png)

## See Also
* <a href="https://github.com/yjg30737/pyqt-timer-label.git">pyqt-timer-label</a>



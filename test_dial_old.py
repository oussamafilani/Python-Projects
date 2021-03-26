from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow, QAction, QMenu, QApplication
import sys


class Mon_dial(QtWidgets.QDial):
    atzero = QtCore.Signal(int)

    def __init__(self, parent=None):
        super(Mon_dial, self).__init__(parent)
        self.valueChanged.connect(self.checkzero)
        self.value = 0
        self.ord = None

    def checkzero(self, n):
        if n == 99:
            self.ord = 99
        if n == 1:
            self.ord = 1
        if n == 0:
            if self.ord == 99:
                self.value += 1
            elif self.ord == 1:
                self.value -= 1
            self.atzero.emit(self.value)


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        dial = Mon_dial()
        print(dial.checkzero)
        dial.setNotchesVisible(True)
        spinbox = QtWidgets.QSpinBox()
        spinbox_mondial = QtWidgets.QSpinBox()
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        layout.addWidget(spinbox_mondial)
        dial.valueChanged.connect(spinbox.setValue)
        dial.atzero.connect(spinbox_mondial.setValue)
        spinbox.valueChanged.connect(dial.setValue)
        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fr = Form()
    sys.exit(app.exec_())
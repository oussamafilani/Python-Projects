from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow, QAction, QMenu, QApplication
import sys


# class MyDialBox(QtWidgets.QDial):
#     atzero = QtCore.Signal()
#
#     def __init__(self):
#         pass
#
#     def check_zero(self):
#         pass


class Form(QtWidgets.QDialog):

    atzero = QtCore.Signal(int)

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.dial = QtWidgets.QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setNotchesVisible(True)
        self.dial.valueChanged.connect(self.change_value)
        # if self.dial.value() == 0:
        #     self.checkZero

        self.spinbox = QtWidgets.QSpinBox()
        self.spinbox_Compt = QtWidgets.QSpinBox()
        layout = QtWidgets.QHBoxLayout()

        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)
        layout.addWidget(self.spinbox_Compt)

        self.setLayout(layout)
        self.show()

    def change_value(self):
        self.spinbox.setValue(self.dial.value())

    def checkZero(self, n=0):
        print("On est dans checkzero")
        self.atzero.connect(self.pass_zero)
        self.atzero.emit()

    def pass_zero(self):
        self.spinbox_Compt.setValue(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fr = Form()
    sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys


class Form(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.dial = QtWidgets.QDial()
        self.dial.setNotchesVisible(True)
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(10)
        self.dial.valueChanged.connect(self.dial_changed)

        btn = QtWidgets.QPushButton('ok')
        btn.clicked.connect(self.dial_changed)
        self.label = QtWidgets.QLabel()
        self.spinbox = QtWidgets.QSpinBox()
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(btn)
        layout.addWidget(self.label)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)
        self.show()

    def dial_changed(self):
        #valeur = self.dial.value()
        #self.label.setText(str(self.dial.value()))
        self.spinbox.setValue(self.dial.value())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Form()
    sys.exit(app.exec_())
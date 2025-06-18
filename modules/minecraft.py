from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import (QApplication, QDialog, QLayout, QGridLayout,
                               QMessageBox, QGroupBox, QSpinBox, QSlider,
                               QProgressBar, QDial, QDialogButtonBox,
                               QComboBox, QLabel, QMainWindow)

class Minecraft(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text = QtWidgets.QLabel("Minecraft",
                                     alignment=QtCore.Qt.AlignCenter)


        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
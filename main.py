import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (QApplication, QDialog, QLayout, QGridLayout,
                               QMessageBox, QGroupBox, QSpinBox, QSlider,
                               QProgressBar, QDial, QDialogButtonBox, QFrame,
                               QComboBox, QLabel, QMainWindow,QHBoxLayout, QVBoxLayout, QPushButton)
from PySide6.QtGui import QScreen
from modules import minecraft, MyWidget, writing


class ApplicationFrame(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # self.button = QtWidgets.QPushButton("Next Window")

        self._widgets = []
        self._widgets = [minecraft.Minecraft(),writing.Writing(),MyWidget.MyWidget()]
        self.curr_page = 0

        self.create_group_box()
        self.create_left_button_box()
        self.create_right_button_box()



        main_layout = QHBoxLayout()
        # main_layout.addWidget(self._left_button_box, 0, 0)
        # main_layout.addWidget(self._group_box, 0, 1)
        # main_layout.addWidget(self._right_button_box, 0, 2)
        # main_layout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        # main_layout.maximumSize

        main_layout.addLayout(self._left_button_box)
        main_layout.addLayout(self._pages_layout, stretch=4)
        main_layout.addLayout(self._right_button_box)



        self._main_layout = main_layout
        self.setLayout(self._main_layout)

        self.setWindowTitle("Dynamic Layouts")



    def moveright(self):
        count = len(self._widgets)

        for widget in self._widgets:
            widget.hide()

        self.curr_page += 1
        self._widgets[self.curr_page % count].show()

          
    def moveleft(self):
        count = len(self._widgets)
        for widget in self._widgets:
            widget.hide()
        self.curr_page -= 1

        self._widgets[self.curr_page % count].show()

    def create_group_box(self):
        # self._group_box = QGroupBox("Pages")

        # self._widgets.append(minecraft.Minecraft())
        # self._widgets.append(writing.Writing())
        # self._widgets.append(MyWidget.MyWidget())

        # self._widgets.append(QSpinBox())
        # self._widgets.append(QSlider())
        # self._widgets.append(QDial())
        # self._widgets.append(QProgressBar())
        count = len(self._widgets)

        self._pages_layout = QHBoxLayout()
#        self._pages_layout.setColumnMinimumWidth(0,200)
#        self._pages_layout.setRowMinimumHeight(0,200)
        # self._pages_layout.addStretch()

        # self._group_box.setLayout(self._pages_layout)

        for widget in self._widgets:
            # print(widget)
            self._pages_layout.addWidget(widget)
            widget.hide()

        self._widgets[self.curr_page].show()



    def create_left_button_box(self):
        self._left_button_box = QVBoxLayout()

        lefticon = QtGui.QIcon.fromTheme(QtGui.QIcon.ThemeIcon.GoPrevious)

        leftbutton = QPushButton(lefticon, "")
        leftbutton.clicked.connect(self.moveleft)
        leftbutton.setStyleSheet("border :0px solid ;")
        SrcSize = QScreen.availableGeometry(QApplication.primaryScreen())
        buttonSize = QSize(50,int(SrcSize.height() * 0.8))
        leftbutton.setMaximumHeight(SrcSize.height() * 0.8)    
        self._left_button_box.addWidget(leftbutton)
        
        # self._left_button_box = QDialogButtonBox(centerButtons=True)

        # # close_button = self._button_box.addButton(QDialogButtonBox.StandardButton.Close)
        # # help_button = self._button_box.addButton(QDialogButtonBox.StandardButton.Help)
        # # rotate_widgets_button = self._button_box.addButton(
        # #     "Rotate &Widgets", QDialogButtonBox.ButtonRole.ActionRole)
        # leftbutton = self._left_button_box.addButton("Left", QDialogButtonBox.ButtonRole.ActionRole)
        # leftbutton.clicked.connect(self.moveleft)


        # rotate_widgets_button.clicked.connect(self.rotate_widgets)
        # close_button.clicked.connect(self.close)
        # help_button.clicked.connect(self.show_help)


    def create_right_button_box(self):
        self._right_button_box = QVBoxLayout()
        righticon = QtGui.QIcon.fromTheme(QtGui.QIcon.ThemeIcon.GoNext)
        rightbutton = QPushButton(righticon, "")
        rightbutton.clicked.connect(self.moveright)
        rightbutton.setStyleSheet("border :0px solid ;")
        SrcSize = QScreen.availableGeometry(QApplication.primaryScreen())
        rightbutton.setMaximumHeight(SrcSize.height() * 0.8)         
        self._right_button_box.addWidget(rightbutton)

        
        # self._right_button_box = QDialogButtonBox()

        # rightbutton = self._right_button_box.addButton("Right", QDialogButtonBox.ButtonRole.ActionRole)
        # rightbutton.clicked.connect(self.moveright)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    # dialog = ApplicationFrame()
    # dialog.exec()

    # app = QtWidgets.QApplication([])

    widget = ApplicationFrame()
    widget.resize(800, 600)
    widget.show()



    sys.exit(app.exec())
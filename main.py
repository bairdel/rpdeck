import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (QApplication, QLayout, QGridLayout, QFrame,
                               QLabel, QMainWindow, 
                               QHBoxLayout, QVBoxLayout, QPushButton)
from PySide6.QtGui import QScreen
from modules import minecraft, MyWidget, writing


class ApplicationFrame(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self._widgets = [minecraft.Minecraft(),writing.Writing(),MyWidget.MyWidget()]
        self.curr_page = 0

        # create the two places for arrows at sides
        self.create_group_box()
        self.create_left_button_box()
        self.create_right_button_box()

        # add created layouts to main layout
        main_layout = QHBoxLayout()
        main_layout.addLayout(self._left_button_box)
        main_layout.addLayout(self._pages_layout, stretch=4)
        main_layout.addLayout(self._right_button_box)

        self._main_layout = main_layout
        self.setLayout(self._main_layout)

        self.setWindowTitle("RP-DECK")



    def moveright(self):
        """change to the main widget next in list"""
        count = len(self._widgets)

        # hide all widgets in view
        for widget in self._widgets:
            widget.hide()

        self.curr_page += 1
        # show only next widget
        self._widgets[self.curr_page % count].show()

          
    def moveleft(self):
        """change to the main widget previous in list"""
        count = len(self._widgets)
        for widget in self._widgets:
            widget.hide()
        self.curr_page -= 1

        self._widgets[self.curr_page % count].show()

    def create_group_box(self):
        """add all widgets to one layout and hide all"""
        self._pages_layout = QHBoxLayout()

        for widget in self._widgets:
            self._pages_layout.addWidget(widget)
            widget.hide()

        self._widgets[self.curr_page].show()



    def create_left_button_box(self):
        self._left_button_box = QVBoxLayout()

        # create button
        lefticon = QtGui.QIcon.fromTheme(QtGui.QIcon.ThemeIcon.GoPrevious)
        leftbutton = QPushButton(lefticon, "")
        leftbutton.clicked.connect(self.moveleft)

        # formatting options - no border + height is most of window
        leftbutton.setStyleSheet("border :0px solid ;")
        SrcSize = QScreen.availableGeometry(QApplication.primaryScreen())
        leftbutton.setMaximumHeight(SrcSize.height() * 0.8)    

        self._left_button_box.addWidget(leftbutton)
        
    def create_right_button_box(self):
        self._right_button_box = QVBoxLayout()
        righticon = QtGui.QIcon.fromTheme(QtGui.QIcon.ThemeIcon.GoNext)
        rightbutton = QPushButton(righticon, "")
        rightbutton.clicked.connect(self.moveright)

        rightbutton.setStyleSheet("border :0px solid ;")
        SrcSize = QScreen.availableGeometry(QApplication.primaryScreen())
        rightbutton.setMaximumHeight(SrcSize.height() * 0.8)  

        self._right_button_box.addWidget(rightbutton)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = ApplicationFrame()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
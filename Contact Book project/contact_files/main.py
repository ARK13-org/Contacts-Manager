""" this module provides contact application """

import sys
from PySide6.QtWidgets import QApplication
from .views import Window
from .database import creatConnection

def main() :
    """ contacts main function """
app = QApplication(sys.argv)
if not creatConnection('contacts.sqlite') :
    sys.exit(1)
win = Window()
win.show()
sys.exit(app.exec())
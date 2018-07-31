# MIT License
# 
# Copyright (c) 2017 Arkadiusz Netczuk <dev.arnet@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#


import sys

try:
    from PyQt5.QtWidgets import QApplication
#     from PyQt5 import uic
except ImportError as e:
    ### No module named <name>
    print(e)
    exit(1)

import uiloader



Ui_TargetClass, QtBaseClass = uiloader.loadUi("main_window.ui")


class MainWindow(QtBaseClass):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_TargetClass()
        self.ui.setupUi(self)
        
        # Make some local modifications.
#         self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")
         
        # Connect up the buttons.
#         self.ui.okButton.clicked.connect(self.accept)
#         self.ui.cancelButton.clicked.connect(self.reject)


def execApp():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.show()
    sys.exit(app.exec_())

import sys
sys.path.append("..")
import os
import serial

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import unicodedata

from Compiler.compiler import compile

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        screenSize = QApplication.desktop().screenGeometry(QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos()))
        self.setGeometry(70, 70, screenSize.width()*.6, screenSize.height()*.7)
        self.setWindowTitle("LedCube IDE")
        self.setWindowIcon(QIcon('cubeIcon.png'))

        runCode = QAction('Run', self)
        runCode.setShortcut("Ctrl+R")
        runCode.triggered.connect(self.runCode)

        openFile = QAction('Open', self)
        openFile.setShortcut("Ctrl+F")
        openFile.triggered.connect(self.openFile)

        save = QAction('Save As', self)
        save.setShortcut("Ctrl+S")
        save.triggered.connect(self.saveFile)

        exit = QAction('Exit', self)
        exit.setShortcut("Ctrl+Q")
        exit.triggered.connect(self.exit)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        fileMenu.addAction(runCode)
        fileMenu.addAction(openFile)
        fileMenu.addAction(save)
        fileMenu.addAction(exit)

        self.editor = QTextEdit()
        self.editor.setFontPointSize(12)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setLineWrapMode(QTextEdit.NoWrap)
        self.log.setMaximumHeight(100)
        self.log.setFontPointSize(11)


        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        layout.addWidget(self.log)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.restoreAutoSave()

        self.center()
        self.show()

    def restoreAutoSave(self):
        file = open('autosave.txt', "r")
        code = ""
        with file:
            code = file.read()
        file.close()
        self.editor.setText(code)

    def runCode(self):
        self.log.clear()
        unicodeCode = self.editor.toPlainText()
        code = unicodedata.normalize('NFKD', unicodeCode).encode('ascii','ignore')
        response = compile(code)
        self.log.setText(response)
    
    def openFile(self):
        name, _ = QFileDialog.getOpenFileName(self, "Open File", os.path.abspath('.//Samples//'))
        if not name == u'':
            file = open(name,'r')
            with file:
                text = file.read()
                self.editor.setText(text)
    
    def saveFile(self):
        name, _ = QFileDialog.getSaveFileName(self, "Save File", os.path.abspath('.//Samples//'), options=QFileDialog.DontUseNativeDialog)
        if not name == u'':
            file = open(name, 'w')
            text = self.editor.toPlainText()
            file.write(text)
            file.close()

    def exit(self):
        file = open('autosave.txt', "w")
        file.write(self.editor.toPlainText())
        file.close()
        sys.exit()

    def closeEvent(self, event):
        file = open('autosave.txt', "w")
        file.write(self.editor.toPlainText())
        file.close()
        event.accept()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

def runIDE():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    gui = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    runIDE()

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(70, 70, 800, 400)
        self.setWindowTitle("LedCube IDE")
        self.setWindowIcon(QIcon('cubeIcon.png'))

        exitAction = QAction("Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip('Leave The App')
        exitAction.triggered.connect(self.close)

        runCodeAction = QAction('Run', self)
        runCodeAction.setShortcut("Ctrl+R")
        runCodeAction.triggered.connect(self.runCode)

        openFileAction = QAction('Open File', self)
        openFileAction.setShortcut("Ctrl+F")
        openFileAction.triggered.connect(self.openFile)

        saveFileAction = QAction('Save File', self)
        saveFileAction.setShortcut("Ctrl+S")
        saveFileAction.triggered.connect(self.saveFile)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        fileMenu.addAction(runCodeAction)
        fileMenu.addAction(openFileAction)
        fileMenu.addAction(saveFileAction)
        fileMenu.addAction(exitAction)

        self.editor = QTextEdit()
        self.editor.setFontPointSize(12)
        self.setCentralWidget(self.editor)

        self.show()


    def runCode(self):
        code = self.editor.toPlainText()
        print code
    
    def openFile(self):
        name, _ = QFileDialog.getOpenFileName(self, "Open File")
        file = open(name,'r')
        with file:
            text = file.read()
            print "ok"
            self.editor.setText(text)
    
    def saveFile(self):
        name, _ = QFileDialog.getSaveFileName(self, "Save File", options=QFileDialog.DontUseNativeDialog)
        file = open(name, 'w')
        text = self.editor.toPlainText()
        file.write(text)
        file.close()

    def close(self):
        sys.exit()

def runIDE():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    gui = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    runIDE()
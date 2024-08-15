# Literally so ass but idgaf

import requests, sys, random, urllib.request
from PySide6 import QtCore, QtWidgets, QtGui
from bs4 import BeautifulSoup

tit = "Soundcloud Artwork Retriever"

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(tit)
        
        self.errMsg = QtWidgets.QMessageBox()
        self.errMsg.setWindowTitle(tit)
        self.errMsg.setIcon(QtWidgets.QMessageBox.Critical)
        
        self.sucMessage = QtWidgets.QMessageBox()
        self.sucMessage.setWindowTitle(tit)
        self.sucMessage.setText("Successfully downloaded image!")
        
        button = QtWidgets.QPushButton("Download Artwork")
        self.link = QtWidgets.QLineEdit("Link")
        self.picName = QtWidgets.QLineEdit("File Name")
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.link)
        layout.addWidget(self.picName)
        layout.addWidget(button)
        
        button.clicked.connect(self.retrieve)
    
    
    def retrieve(self):
        url = self.link.text()
            
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, features="html.parser")
            src = soup.find("img", {"itemprop":"image"})['src']
            if not src == None:
                urllib.request.urlretrieve(src, f"Artwork/{self.picName.text()}.png")
                self.sucMessage.exec()
            else:
                self.errMsg.setText("Unable to find image!")
                self.errMsg.exec()
        except requests.exceptions.MissingSchema:
            self.errMsg.setText("Missing schema.")
            self.errMsg.exec()
        except:
            self.errMsg.setText("Unknown error. Is the link correct?")
            self.errMsg.exec()

        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Widget()
    widget.resize(350,100)
    widget.show()
    sys.exit(app.exec())


# importing the required libraries
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
import sys
from Flogin import Ui_MainWindow
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
         
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit_3.returnPressed.connect(self.buton)
        self.ui.pushButton_login.clicked.connect(self.buton)
        self.show()
    
    def buton(self):
        if  not self.ui.lineEdit_3.text():
            if not self.ui.lineEdit.text():
                self.ui.textEdit.setText("\n\n \t Lütfen ilgili yerleri doldurunuz...")
            else:
                tstop = float(self.ui.lineEdit.text().replace(",","."))
                titop = float(self.ui.lineEdit_4.text().replace(",","."))
                rstop = float(self.ui.lineEdit_user.text().replace(",","."))
                ritop = float(self.ui.lineEdit_2.text().replace(",","."))
                try:
                    ceza = ((rstop-ritop)/(tstop-titop))*100
                    if  ceza >= 20 :
                        self.ui.textEdit.setStyleSheet("background-color: rgb(255, 0, 0);")
                        self.ui.textEdit.setText("Reaktif : "+ str(ceza) +"\n \n " + "\n\n\n\t\t Reaktif Cezada..."  )
                    else:
                        self.ui.textEdit.setStyleSheet("background-color: rgb(85, 255, 0);")
                        self.ui.textEdit.setText("Reaktif : "+ str(ceza) +"\n \n"+"Cezada Değil..." )
                except ZeroDivisionError:
                    self.ui.textEdit.setText("\n\n\t\tTesiste tüketim yok..." )
        else:
            try:
                a = self.ui.lineEdit_3.text()
                a = a.split()
                reaktif = ((float(a[6])-float(a[17])) / (float(a[2])-float(a[13])))*100
                kapasitif = ((float(a[7])-float(a[18])) / (float(a[2])-float(a[13])))*100
                
                if reaktif > 20 and kapasitif >15:
                    self.ui.textEdit.setStyleSheet("background-color: rgb(255, 0, 0);")
                    self.ui.textEdit.setText("İndüktif : "+ str(reaktif) +"\n \n"+"Kapasitif : " +str(kapasitif)+ "\n\n\t\t İndüktif Ve Kapasitif Cezada..."  )
                elif  reaktif >= 20 :
                    self.ui.textEdit.setStyleSheet("background-color: rgb(255, 0, 0);")
                    self.ui.textEdit.setText("İndüktif : "+ str(reaktif) +"\n \n"+"Kapasitif : " +str(kapasitif)+ "\n\n\n\t\t İndüktif Cezada..."  )
                elif kapasitif >=15:
                    self.ui.textEdit.setStyleSheet("background-color: rgb(255, 0, 0);")
                    self.ui.textEdit.setText("İndüktif : "+ str(reaktif) +"\n \n"+"Kapasitif : " +str(kapasitif)+ "\n\n\t\t Kapasitif Cezada..."  )
                
                else:
                    self.ui.textEdit.setStyleSheet("background-color: rgb(85, 255, 0);")
                    self.ui.textEdit.setText("Reaktif : "+ str(reaktif) +"\n \n"+"Kapasitif : " +str(kapasitif)  )
            except ZeroDivisionError:
                self.ui.textEdit.setText("\n\n\tTesiste tüketim yok..." )
            except IndexError:
                self.ui.textEdit.setText("\n\n\tLütfen ilgili format'ta veri giriniz..")

if __name__ == "__main__":   
    # create pyqt5 app
    App = QApplication(sys.argv)
    # create the instance of our Window
    window = Window()

    # start the app
    sys.exit(App.exec())
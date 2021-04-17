# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QInputDialog,QLineEdit,QFileDialog
import sys
import sqlite3


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(400, 300)
        self.setToolTip("")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(297, 33, 100, 110))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 251, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(280, 20, 111, 21))
        self.pushButton.setToolTip("Sql Bazasını daxil et")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 220, 111, 31))
        self.pushButton_2.setToolTip("Sql sorğusu yarat")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 220, 111, 31))
        self.pushButton_3.setToolTip("Sql sorğusunun düzgünlüyünü yoxla")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 50, 111, 21))
        self.pushButton_4.setToolTip("Sql melumat bazasının melumatlarını hesabla")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 260, 111, 31))
        self.pushButton_5.setToolTip("Sorğuları temizle")
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 271, 141))
        self.groupBox.setObjectName("groupBox")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 251, 111))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(290, 100, 100, 110))
        self.textBrowser.setObjectName("textBrowser")
        self.label.raise_()
        self.groupBox.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Browse"))
        self.pushButton.clicked.connect(self.BrowseFile)
        self.pushButton_2.setText(_translate("Dialog", "SQL Sorğu..."))
        self.pushButton_2.clicked.connect(self.QuerySql)
        self.pushButton_3.setText(_translate("Dialog", "Sorğunu yoxla"))
        self.pushButton_4.setText(_translate("Dialog", "Hesabla"))
        self.pushButton_4.clicked.connect(self.SqlTonHa)
        self.pushButton_5.setText(_translate("Dialog", "Sorğunu sil"))
        self.groupBox.setTitle(_translate("Dialog", "SQL Expression"))
        self.label.setText(_translate("Dialog", "Bildiriş paneli"))

    def QuerySql(self):
        dialogg = Ui_Dialogg()

    def BrowseFile(self):
        filename = QFileDialog.getOpenFileName()
        filename = filename[0]
        self.lineEdit.setText(filename)

        

    def SqlTonHa(self):
        connect = self.lineEdit.text()
        try:
            con = sqlite3.connect(connect)
            con2 = sqlite3.connect(r"C:\Users\umaro\OneDrive\Desktop\Part.db")
            information = []

            cursor = con.cursor()
            cursor2 = con2.cursor()
            cursor.execute("SELECT * FROM DatabaseD")
            cursor2.execute("""CREATE TABLE IF NOT EXISTS Part (Yarimtip TEXT,Humus_20_ton_ha INT, Humus_50_ton_ha INT, Humus_100_ton_ha INT,Azot_20_ton_ha INT, Azot_50_ton_ha INT,  Fosfor_20_ton_ha INT, Fosfor_50_ton_ha INT)""")
            data = cursor.fetchall()
            information.extend(data)

            for k in information:
                if k[1]== "Çimli-torflu dağ-çəmən" or "Çimli dağ-çəmən" or "Qaramtıl dağ-çəmən" or "Bozqır dağ-çəmən":
                    yarimtip = k[1]
                    #print(yarimtip)
                    humus20_ton = (k[2] * 0.87 * 2000)/100
                    humus50_ton = (k[3] * 1.04 * 5000)/100
                    humus100_ton = (k[4] * 1.15 * 10000)/100

                    azot20_ton = (k[5] * 0.87 * 2000)/100
                    azot50_ton = (k[6] * 1.04 * 5000)/100

                    fosfor20_ton = (k[8] * 0.87 * 2000)/100
                    fosfor50_ton = (k[9] * 1.04 * 5000)/100

                if k[1]== "Tipik qonur dağ-meşə" or "Zəif doymuş (lösləşmiş) qonur dağ-meşə" or "Karbonat qalıqlı qonur dağ-meşə"or "Bozqırlaşmış qonur dağ-meşə" or "Podzollaşmış qonur dağ-meşə":
                    yarimtip = k[1]

                    humus20_ton = (k[2] * 1.02 * 2000)/100
                    humus50_ton = (k[3] * 1.12 * 5000)/100
                    humus100_ton = (k[4] * 1.22 * 10000)/100

                    azot20_ton = (k[5] * 1.02 * 2000)/100
                    azot50_ton = (k[6] * 1.12 * 5000)/100

                    fosfor20_ton = (k[8] * 1.02 * 2000)/100
                    fosfor50_ton = (k[9] * 1.12 * 5000)/100

                if k[1] == "Yuyulmuş qəhvəyi dağ meşə" or "Tipik qəhvəyi dağ meşə" or "Karbonatlı qəhvəyi dağ meşə":
                    yarimtip = k[1]
                    humus20_ton = (k[2] * 1.18 * 2000)/100
                    humus50_ton = (k[3] * 1.25 * 5000)/100
                    humus100_ton = (k[4] * 1.27 * 10000)/100

                    azot20_ton = (k[5] * 1.18 * 2000)/100
                    azot50_ton = (k[6] * 1.25 * 5000)/100

                    fosfor20_ton = (k[8] * 1.18 * 2000)/100
                    fosfor50_ton = (k[9] * 1.25 * 5000)/100

                if k[1] == "Yuyulmuş dağ qara" or "Adi dağ qara" or "Karbonatlı dağ qara" or "Bərkimiş dağ qara":
                    yarimtip = k[1]
                    humus20_ton = (k[2] * 1.08 * 2000)/100
                    humus50_ton = (k[3] * 1.15 *5000)/100
                    humus100_ton = (k[4] * 1.24 * 10000)/100

                    azot20_ton = (k[5] * 1.08 * 2000)/100
                    azot50_ton = (k[6] * 1.15 * 5000)/100

                    fosfor20_ton = (k[8] * 1.08 * 2000)/100
                    fosfor50_ton = (k[9] * 1.15 * 5000)/100

                if k[1] == "Sarı dağ-meşə" or "Podzollu-sarı" or "Podzollu-qleyli-sarı" or "Sarı-qleyli ":
                    yarimtip = k[1]
                    humus20_ton = (k[2] * 1.18 * 2000)/100
                    humus20_ton = (k[3] * 1.28 * 5000)/100
                    humus100_ton = (k[4] * 1.36 * 10000)/100

                    azot20_ton = (k[5] * 1.18 * 2000)/100
                    azot50_ton = (k[6] * 1.28 * 5000)/100

                    fosfor20_ton = (k[8] * 1.18 * 2000)/100
                    fosfor50_ton = (k[9] * 1.28 * 5000)/100

                if k[1] == "Səthdən çəmənləşmiş şabalıdı" or "Çəmən-qəhvəyi" :
                    yarimtip = k[1]
                    humus20_ton = (k[2] * 1.16 * 2000)/100
                    humus50_ton = (k[3] * 1.26 * 5000)/100
                    humus100_ton = (k[4] * 1.32 * 10000)/100

                    azot20_ton = (k[5] * 1.16 * 2000)/100
                    azot50_ton = (k[6] * 1.26 * 5000)/100

                    fosfor20_ton = (k[8] * 1.16 * 2000)/100
                    fosfor50_ton = (k[9] * 1.26 * 5000)/100

                if k[1] == "Tünd şabalıdı" or "Adi şabalıdı" or "Açıq şabalıdı" or "'gəcli' şabalıdı":
                    yarimtip = k[1]
                    humus20_ton = (k[2] * 1.2 * 2000)/100
                    humus50_ton = (k[3] * 1.26 * 5000)/100
                    humus100_ton = (k[4] * 1.3 * 10000)/100

                    azot20_ton = (k[5] * 1.2 * 2000)/100
                    azot50_ton = (k[6] * 1.26 * 5000)/100

                    fosfor20_ton = (k[8] * 1.2 * 2000)/100
                    fosfor50_ton = (k[9] * 1.26 * 5000)/100

                if k[1] == "Səthdən çəmənləşmiş şabalıdı" or "Çəmənləşmiş şabalıdı" or "Çəmən şabalıdı" :
                    yarimtip = k[1]
                    humus20_ton = (k[2] * 1.16 * 2000)/100
                    humus50_ton = (k[3] * 1.24 * 5000)/100
                    humus100_ton = (k[4] * 1.3 * 10000)/100

                    azot20_ton = (k[5] * 1.16 * 2000)/100
                    azot50_ton = (k[6] * 1.24 * 5000)/100

                    fosfor20_ton = (k[8] * 1.16 * 2000)/100
                    fosfor50_ton = (k[9] * 1.24 * 5000)/100

                if k[1] == "Açıq-boz" or "Adi-boz" or "Qədimdən suvarılan boz" or "İbtidai boz":
                    yarimtip = k[1]
                    humus20_ton = (k[2] * 1.25 * 2000)/100
                    humus50_ton = (k[3] * 1.3 * 5000)/100
                    humus100_ton = (k[4] * 1.34 * 10000)/100

                    azot20_ton = (k[5] * 1.25 * 2000)/100
                    azot50_ton = (k[6] * 1.3 * 5000)/100

                    fosfor20_ton = (k[8] * 1.25 * 2000)/100
                    fosfor50_ton = (k[9] * 1.3 * 5000)/100

                if k[1] == "Çürüntülü çəmən-bataqlıq" or "Lilli çəmənbataqlıq":
                    yarimtip = k[1]
                    humus20_ton = (k[2] * 1.1 * 2000)/100
                    humus50_ton = (k[3] * 1.16 * 5000)/100
                    humus100_ton = (k[4] * 1.23 * 10000)/100

                    azot20_ton = (k[5] * 1.1 * 2000)/100
                    azot50_ton = (k[6] * 1.16 * 5000)/100

                    fosfor20_ton = (k[8] * 1.1 * 2000)/100
                    fosfor50_ton = (k[9] * 1.16 * 5000)/100

                if k[0] == "Dağ-çəmən" and k[1] == "":
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 0.87 * 2000) / 100
                    humus50_ton = (k[3] * 1.04 * 5000) / 100
                    humus100_ton = (k[4] * 1.15 * 10000) / 100

                    azot20_ton = (k[5] * 0.87 * 2000) / 100
                    azot50_ton = (k[6] * 1.04 * 5000) / 100

                    fosfor20_ton = (k[8] * 0.87 * 2000) / 100
                    fosfor50_ton = (k[9] * 1.04 * 5000) / 100

                if k[0] == "Qonur dağ-meşə" and k[1] == "":
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.02 * 2000) / 100
                    humus50_ton = (k[3] * 1.12 * 5000) / 100
                    humus100_ton = (k[4] * 1.22 * 10000) / 100

                    azot20_ton = (k[5] * 1.02 * 2000) / 100
                    azot50_ton = (k[6] * 1.12 * 5000) / 100

                    fosfor20_ton = (k[8] * 1.02 * 2000) / 100
                    fosfor50_ton = (k[9] * 1.12 * 5000) / 100

                if k[0] == "Qəhvəyi dağ-meşə" and k[1] == "":
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.18 * 2000) / 100
                    humus50_ton = (k[3] * 1.25 * 5000) / 100
                    humus100_ton = (k[4] * 1.27 * 10000) / 100

                    azot20_ton = (k[5] * 1.18 * 2000) / 100
                    azot50_ton = (k[6] * 1.25 * 5000) / 100

                    fosfor20_ton = (k[8] * 1.18 * 2000) / 100
                    fosfor50_ton = (k[9] * 1.25 * 5000) / 100

                if k[0] == "Bozqırlaşmış dağ-qəhvəyi" and (k[1] == "" or k[1] == "Yarımtipi yoxdur"):
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.11 * 2000)/100
                    humus50_ton = (k[3] * 1.21 * 5000)/100
                    humus100_ton = (k[4] * 1.3 * 10000)/100

                    azot20_ton = (k[5] * 1.11 * 2000)/100
                    azot50_ton = (k[6] * 1.21 * 5000)/100

                    fosfor20_ton = (k[8] * 1.11 *2000)/100
                    fosfor50_ton = (k[9] * 1.21 * 5000)/100

                if k[0] == "Dağ boz-qəhvəyi" and (k[1] == "" or k[1] == "Yarımtipi yoxdur"):
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.19 * 2000)/100
                    humus50_ton = (k[3] * 1.29 * 5000)/100
                    humus100_ton = (k[4] * 1.32 * 10000)/100

                    azot20_ton = (k[5] * 1.19 * 2000)/100
                    azot50_ton = (k[6] * 1.29 * 5000)/100

                    fosfor20_ton = (k[8] * 1.19 * 2000)/100
                    fosfor50_ton = (k[9] * 1.29 * 5000)/100

                if k[0] == "Dağ qaratorpaq" and k[1] == "":
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.08 * 2000)/100
                    humus50_ton = (k[3] * 1.15 *5000)/100
                    humus100_ton = (k[4] * 1.24 * 10000)/100

                    azot20_ton = (k[5] * 1.08 * 2000)/100
                    azot50_ton = (k[6] * 1.15 * 5000)/100

                    fosfor20_ton = (k[8] * 1.08 * 2000)/100
                    fosfor50_ton = (k[9] * 1.15 * 5000)/100

                if k[0] == "Dağ şabalıdı" and (k[1] == "" or k[1] == "Yarımtipi yoxdur"):
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.17 * 2000)/100
                    humus50_ton = (k[3] * 1.21 * 5000)/100
                    humus100_ton = (k[4] * 1.31 * 10000)/100

                    azot20_ton = (k[5] * 1.17 * 2000)/100
                    azot50_ton = (k[6] * 1.21 * 5000)/100

                    fosfor20_ton = (k[8] * 1.17 * 2000)/100
                    fosfor50_ton = (k[9] * 1.21 * 5000)/100

                if k[0] == "Sarı" and k[1] == "":
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.18 * 2000)/100
                    humus50_ton = (k[3] * 1.28 * 5000)/100
                    humus100_ton = (k[4] * 1.36 * 10000)/100

                    azot20_ton = (k[5] * 1.18 * 2000)/100
                    azot50_ton = (k[6] * 1.28 * 5000)/100

                    fosfor20_ton = (k[8] * 1.18 * 2000)/100
                    fosfor50_ton = (k[9] * 1.28 * 5000)/100

                if k[0] == "Çəmən-qəhvəyi" and k[1] == "":
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.16 * 2000)/100
                    humus50_ton = (k[3] * 1.26 * 5000)/100
                    humus100_ton = (k[4] * 1.32 * 10000)/100

                    azot20_ton = (k[5] * 1.16 * 2000)/100
                    azot50_ton = (k[6] * 1.26 * 5000)/100

                    fosfor20_ton = (k[8] * 1.16 * 2000)/100
                    fosfor50_ton = (k[9] * 1.26 * 5000)/100

                if k[0] == "Şabalıdı" and k[1] == "":
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.2 * 2000)/100
                    humus50_ton = (k[3] * 1.26 * 5000)/100
                    humus100_ton = (k[4] * 1.3 * 10000)/100

                    azot20_ton = (k[5] * 1.2 * 2000)/100
                    azot50_ton = (k[6] * 1.26 * 5000)/100

                    fosfor20_ton = (k[8] * 1.2 * 2000)/100
                    fosfor50_ton = (k[9] * 1.26 * 5000)/100

                if k[0] == "Çəmən-şabalıdı" and k[1] == "":
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.16 * 2000)/100
                    humus50_ton = (k[3] * 1.24 * 5000)/100
                    humus100_ton = (k[4] * 1.3 * 10000)/100

                    azot20_ton = (k[5] * 1.16 * 2000)/100
                    azot50_ton = (k[6] * 1.24 * 5000)/100

                    fosfor20_ton = (k[8] * 1.16 * 2000)/100
                    fosfor50_ton = (k[9] * 1.24 * 5000)/100

                if k[0] == "Boz-qonur" and (k[1] == "" or k[1] == "Yarımtipi yoxdur"):
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.23 * 2000)/100
                    humus50_ton = (k[3] * 1.33 * 5000)/100
                    humus100_ton = (k[4] * 1.4 * 10000)/100

                    azot20_ton = (k[5] * 1.23 * 2000)/100
                    azot50_ton = (k[6] * 1.33 * 5000)/100

                    fosfor20_ton = (k[8] * 1.23 * 2000)/100
                    fosfor50_ton = (k[9] * 1.33 * 5000)/100

                if k[0] == "Boz" and k[1] == "":
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.25 * 2000)/100
                    humus50_ton = (k[3] * 1.3 * 5000)/100
                    humus100_ton = (k[4] * 1.34 * 10000)/100

                    azot20_ton = (k[5] * 1.25 * 2000)/100
                    azot50_ton = (k[6] * 1.3 * 5000)/100

                    fosfor20_ton = (k[8] * 1.25 * 2000)/100
                    fosfor50_ton = (k[9] * 1.3 * 5000)/100

                if k[0] == "Çəmənləşmiş-boz" and (k[1] == "" or k[1] == "Yarımtipi yoxdur"):
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.28 * 2000)/100
                    humus50_ton = (k[3] * 1.36 * 5000)/100
                    humus100_ton = (k[4] * 1.42 * 10000)/100

                    azot20_ton = (k[5] * 1.28 * 2000)/100
                    azot50_ton = (k[6] * 1.36 * 5000)/100

                    fosfor20_ton = (k[8] * 1.28 * 2000)/100
                    fosfor50_ton = (k[9] * 1.36 * 5000)/100

                if k[0] == "Çəmən-boz" and (k[1] == "" or k[1] == "Yarımtipi yoxdur"):
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.19 * 2000)/100
                    humus50_ton = (k[3] * 1.27 * 5000)/100
                    humus100_ton = (k[4] * 1.33 * 10000)/100

                    azot20_ton = (k[5] * 1.19 * 2000)/100
                    azot50_ton = (k[6] * 1.27 * 5000)/100

                    fosfor20_ton = (k[8] * 1.19 * 2000)/100
                    fosfor50_ton = (k[9] * 1.27 * 5000)/100

                if k[0] == "Çəmən-meşə" and (k[1] == "" or k[1] == "Yarımtipi yoxdur"):
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.14 * 2000)/100
                    humus50_ton = (k[3] * 1.24 * 5000)/100
                    humus100_ton = (k[4] * 1.31 * 10000)/100

                    azot20_ton = (k[5] * 1.14 * 2000)/100
                    azot50_ton = (k[6] * 1.24 * 5000)/100

                    fosfor20_ton = (k[8] * 1.14 * 2000)/100
                    fosfor50_ton = (k[9] * 1.24 * 5000)/100

                if k[0] == "Allüvial-çəmən" and (k[1] == "" or k[1] == "Yarımtipi yoxdur"):
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.16 * 2000)/100
                    humus50_ton = (k[3] * 1.23 * 5000)/100
                    humus100_ton = (k[4] * 1.27 * 10000)/100

                    azot20_ton = (k[5] * 1.16 * 2000)/100
                    azot50_ton = (k[6] * 1.23 * 5000)/100

                    fosfor20_ton = (k[8] * 1.16  * 2000)/100
                    fosfor50_ton = (k[9] * 1.23 * 5000)/100

                if k[0] == "Çəmən-bataqlı" and k[1] == "":
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.1 * 2000)/100
                    humus50_ton = (k[3] * 1.16 * 5000)/100
                    humus100_ton = (k[4] * 1.23 * 10000)/100

                    azot20_ton = (k[5] * 1.1 * 2000)/100
                    azot50_ton = (k[6] * 1.16 * 5000)/100

                    fosfor20_ton = (k[8] * 1.1 * 2000)/100
                    fosfor50_ton = (k[9] * 1.16 * 5000)/100

                if k[0] == "Şoranlar" and (k[1] == "" or k[1] == "Yarımtipi yoxdur"):
                    yarimtip = k[0]

                    humus20_ton = (k[2] * 1.28 * 2000)/100
                    humus50_ton = (k[3] * 1.32 * 5000)/100
                    humus100_ton = (k[4] * 1.35 * 10000)/100

                    azot20_ton = (k[5] * 1.28 * 2000)/100
                    azot50_ton = (k[6] * 1.32 * 5000)/100

                    fosfor20_ton = (k[8] * 1.28 * 2000)/100
                    fosfor50_ton = (k[8] * 1.32 * 5000)/100
















                cursor2.execute("""INSERT INTO Part (Yarimtip,Humus_20_ton_ha,Humus_50_ton_ha,Humus_100_ton_ha,Azot_20_ton_ha,Azot_50_ton_ha,Fosfor_20_ton_ha,Fosfor_50_ton_ha) VALUES (?,?,?,?,?,?,?,?)""",(yarimtip,humus20_ton ,humus50_ton,humus100_ton,azot20_ton,azot50_ton,fosfor20_ton,fosfor50_ton))
                con2.commit()
        except:
            self.textBrowser.setText("""Xeta baş verdi. Xetanın baş vermesinin iki sebebi ola biler:\n 1) Sql fayıl daxil edilmemişdir\n 2) Birinci merheleden Sql fayıl alınmamışdır""")

class Ui_Dialogg(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(527, 322)
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(20, 50, 301, 200))
        #self.lineEdit_2.setAlignment("Qt_Alignment=copyright()")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(340, 50, 41, 21))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 121, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 51, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 50, 41, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 80, 41, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 80, 41, 21))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 110, 41, 21))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(390, 110, 41, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 140, 41, 21))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self)
        self.pushButton_8.setGeometry(QtCore.QRect(390, 140, 41, 21))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self)
        self.pushButton_9.setGeometry(QtCore.QRect(340, 170, 41, 21))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self)
        self.pushButton_10.setGeometry(QtCore.QRect(440, 50, 41, 21))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self)
        self.pushButton_11.setGeometry(QtCore.QRect(440, 80, 41, 21))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self)
        self.pushButton_12.setGeometry(QtCore.QRect(440, 110, 41, 21))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self)
        self.pushButton_13.setGeometry(QtCore.QRect(440, 140, 41, 21))
        self.pushButton_13.setObjectName("pushButton_13")
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(340, 200, 181, 87))
        self.textBrowser.setObjectName("textBrowser")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(340, 20, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_14 = QtWidgets.QPushButton(self)
        self.pushButton_14.setGeometry(QtCore.QRect(340, 290, 151, 28))
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(340, 0, 61, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_15 = QtWidgets.QPushButton(self)
        self.pushButton_15.setGeometry(QtCore.QRect(20, 270, 61, 31))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self)
        self.pushButton_16.setGeometry(QtCore.QRect(190, 270, 61, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self)
        self.pushButton_17.setGeometry(QtCore.QRect(260, 270, 61, 31))
        self.pushButton_17.setObjectName("pushButton_17")



        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.exec()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "="))
        self.pushButton.clicked.connect(self.Equal)
        self.label.setText(_translate("Dialog", "SELECT * FROM"))
        self.label_2.setText(_translate("Dialog", "WHERE"))
        self.pushButton_2.setText(_translate("Dialog", "<>"))
        self.pushButton_2.clicked.connect(self.Equal)
        self.pushButton_3.setText(_translate("Dialog", ">"))
        self.pushButton_3.clicked.connect(self.Equal)
        self.pushButton_4.setText(_translate("Dialog", "<"))
        self.pushButton_4.clicked.connect(self.Equal)
        self.pushButton_5.setText(_translate("Dialog", ">="))
        self.pushButton_5.clicked.connect(self.Equal)
        self.pushButton_6.setText(_translate("Dialog", "<="))
        self.pushButton_6.clicked.connect(self.Equal)
        self.pushButton_7.setText(_translate("Dialog", "()"))
        self.pushButton_7.clicked.connect(self.Equal)
        self.pushButton_8.setText(_translate("Dialog", "IS"))
        self.pushButton_8.clicked.connect(self.Equal)
        self.pushButton_9.setText(_translate("Dialog", "IN"))
        self.pushButton_9.clicked.connect(self.Equal)
        self.pushButton_10.setText(_translate("Dialog", "AND"))
        self.pushButton_10.clicked.connect(self.Equal)
        self.pushButton_11.setText(_translate("Dialog", "OR"))
        self.pushButton_11.clicked.connect(self.Equal)
        self.pushButton_12.setText(_translate("Dialog", "NOT"))
        self.pushButton_12.clicked.connect(self.Equal)
        self.pushButton_13.setText(_translate("Dialog", "NULL"))
        self.pushButton_13.clicked.connect(self.Equal)
        self.comboBox.setItemText(0, _translate("Dialog", "Torpaq_adi"))
        self.comboBox.setItemText(1, _translate("Dialog", "Torpaq_Yarım_Tipi"))
        self.comboBox.setItemText(2, _translate("Dialog", "Humus_20"))
        self.comboBox.setItemText(3, _translate("Dialog", "Humus_50"))
        self.comboBox.setItemText(4, _translate("Dialog", "Humus_100"))
        self.comboBox.setItemText(5, _translate("Dialog", "Azot_20"))
        self.comboBox.setItemText(6, _translate("Dialog", "Azot_50"))
        self.comboBox.setItemText(7, _translate("Dialog", "Azot_100"))
        self.comboBox.setItemText(8, _translate("Dialog", "Fosfor_20"))
        self.comboBox.setItemText(9, _translate("Dialog", "Fosfor_50"))
        self.comboBox.setItemText(10, _translate("Dialog", "Fosfor_100"))
        self.comboBox.setItemText(11, _translate("Dialog", "Kalium_20"))
        self.comboBox.setItemText(12, _translate("Dialog", "Kalium_50"))
        self.comboBox.setItemText(13, _translate("Dialog", "Kalium_100"))
        self.pushButton_14.setText(_translate("Dialog", "Unikal Məlumatlara Bax"))
        self.pushButton_14.clicked.connect(self.ShowInfo)
        self.label_3.setText(_translate("Dialog", "Sütun adı:"))
        self.pushButton_15.setText(_translate("Dialog", "Əlavə et"))
        self.pushButton_16.setText(_translate("Dialog", "Təsdiqlə"))
        self.pushButton_17.setText(_translate("Dialog", "Təmizlə"))

    def ShowInfo(self):
        self.textBrowser.clear()
        InfoList = []
        InfoListIndex = []
        Info = []
        BaseName = self.lineEdit.text()
        FilePath = r"C:/Users/umaro/OneDrive/Desktop/"
        con = sqlite3.connect(FilePath +BaseName + ".db")
        select = "SELECT"
        From = "FROM"

        cursor = con.cursor()
        cursor.execute(select + " " + self.comboBox.currentText() + " " + From + " " + BaseName )

        data = cursor.fetchall()
        for s in data:
            if s not in InfoList:
                InfoList.append(s)
                index=InfoList.index(s)
                InfoListIndex.append(index)
        for d in InfoList:
            if self.textBrowser.toPlainText()=="":
                self.textBrowser.setText(str(d[0]))
            else:
                self.textBrowser.setText(self.textBrowser.toPlainText()+" "+"\n"+str(d[0]))




        con.commit()



    def Equal(self):
        btn_text = self.sender().text()
        if self.textEdit.toPlainText()=="":
            self.textEdit.setText(btn_text)
        else:
            self.textEdit.setText(self.textEdit.toPlainText()+btn_text)







def window():
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    sys.exit(app.exec_())
    


if __name__ == "__main__":
    window()
    

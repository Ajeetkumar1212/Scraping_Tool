

import lxml
from multiprocessing import Queue
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import lxml.html as lh



class Ui_MainWindow(object):
    temp = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit\n"
"{\n"
"\n"
"background:rgb(170, 255, 255)\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(600)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.scrapURL)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 18))
        self.menubar.setObjectName("menubar")
        self.menuOTCBB = QtWidgets.QMenu(self.menubar)
        self.menuOTCBB.setObjectName("menuOTCBB")
        self.menuFintel = QtWidgets.QMenu(self.menubar)
        self.menuFintel.setObjectName("menuFintel")
        self.menuFintel_2 = QtWidgets.QMenu(self.menubar)
        self.menuFintel_2.setObjectName("menuFintel_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)




        ##OTCBB MENU BUTTON
        self.actionMost_Active = QtWidgets.QAction(MainWindow)
        self.actionMost_Active.setObjectName("actionMost_Active")
       # self.actionMost_Active.triggered.connect(self.most_Active_func)
        self.actionMost_Active.triggered.connect(self.most_Active_func)


        self.actionBest_Stock = QtWidgets.QAction(MainWindow)
        self.actionBest_Stock.setObjectName("actionBest_Stock")
        self.actionBest_Stock.triggered.connect(self.Best_stocks)

        self.actionTop_EPS_Stocks = QtWidgets.QAction(MainWindow)
        self.actionTop_EPS_Stocks.setObjectName("actionTop_EPS_Stocks")
        self.actionTop_EPS_Stocks.triggered.connect(self.Top_EPS_Stock)

        self.actionWorst_Stock = QtWidgets.QAction(MainWindow)
        self.actionWorst_Stock.setObjectName("actionWorst_Stock")
        self.actionWorst_Stock.triggered.connect(self.WORST_Stock)

        self.actionLow_EPS_STocks = QtWidgets.QAction(MainWindow)
        self.actionLow_EPS_STocks.setObjectName("actionLow_EPS_STocks")
        self.actionLow_EPS_STocks.triggered.connect(self.LOW_EPS)

        self.actionAMEX_Stocks = QtWidgets.QAction(MainWindow)
        self.actionAMEX_Stocks.setObjectName("actionAMEX_Stocks")
        self.actionAMEX_Stocks.triggered.connect(self.AMEX_list)

        self.actionNYSE_Stocks = QtWidgets.QAction(MainWindow)
        self.actionNYSE_Stocks.setObjectName("actionNYSE_Stocks")
        self.actionNYSE_Stocks.triggered.connect(self.NYSE_Stock)

        self.actionNASDAQ_Stocks = QtWidgets.QAction(MainWindow)
        self.actionNASDAQ_Stocks.setObjectName("actionNASDAQ_Stocks")
        self.actionNASDAQ_Stocks.triggered.connect(self.NASDAQ_Stock)

        self.actionStock_List = QtWidgets.QAction(MainWindow)
        self.actionStock_List.setObjectName("actionStock_List")
        self.actionStock_List.triggered.connect(self.Stock_List1)



        ###FINTAL.IO MENU BUTTON
        self.actionBaker_Brothers_Advisors = QtWidgets.QAction(MainWindow)
        self.actionBaker_Brothers_Advisors.setObjectName("actionBaker_Brothers_Advisors")
        self.actionBaker_Brothers_Advisors.triggered.connect(self.baker_bros_advisors)

        self.actionBaupost_Group = QtWidgets.QAction(MainWindow)
        self.actionBaupost_Group.setObjectName("actionBaupost_Group")
        self.actionBaupost_Group.triggered.connect(self.Baupost_Group)


        self.actionBerkshire_Hathaway = QtWidgets.QAction(MainWindow)
        self.actionBerkshire_Hathaway.setObjectName("actionBerkshire_Hathaway")
        self.actionBerkshire_Hathaway.triggered.connect(self.Berkshire_Hathaway)


        self.actionBridgewater_Associates = QtWidgets.QAction(MainWindow)
        self.actionBridgewater_Associates.setObjectName("actionBridgewater_Associates")
        self.actionBridgewater_Associates.triggered.connect(self.Bridgewater_Associates)

        self.actionCascade_Investment = QtWidgets.QAction(MainWindow)
        self.actionCascade_Investment.setObjectName("actionCascade_Investment")
        self.actionCascade_Investment.triggered.connect(self.Cascade_Investment)

        self.actionChatham_Asset_Management = QtWidgets.QAction(MainWindow)
        self.actionChatham_Asset_Management.setObjectName("actionChatham_Asset_Management")
        self.actionChatham_Asset_Management.triggered.connect(self.Chatham_Asset_Management)

        self.actionDuquesne_Family_Office = QtWidgets.QAction(MainWindow)
        self.actionDuquesne_Family_Office.setObjectName("actionDuquesne_Family_Office")
        self.actionDuquesne_Family_Office.triggered.connect(self.Duquesne_Family_Office)

        self.actionGotham_Asset_Management = QtWidgets.QAction(MainWindow)
        self.actionGotham_Asset_Management.setObjectName("actionGotham_Asset_Management")
        self.actionGotham_Asset_Management.triggered.connect(self.Gotham_Asset_Management)

        self.actionMangrove_Partners = QtWidgets.QAction(MainWindow)
        self.actionMangrove_Partners.setObjectName("actionMangrove_Partners")
        self.actionMangrove_Partners.triggered.connect(self.Mangrove_Partners)

        self.actionMelvin_Capital = QtWidgets.QAction(MainWindow)
        self.actionMelvin_Capital.setObjectName("actionMelvin_Capital")
        self.actionMelvin_Capital.triggered.connect(self.Melvin_Capital)

        self.actionPerceptive_Advisors = QtWidgets.QAction(MainWindow)
        self.actionPerceptive_Advisors.setObjectName("actionPerceptive_Advisors")
        self.actionPerceptive_Advisors.triggered.connect(self.Perceptive_Advisors)

        self.actionPoint72_Asset_Management = QtWidgets.QAction(MainWindow)
        self.actionPoint72_Asset_Management.setObjectName("actionPoint72_Asset_Management")
        self.actionPoint72_Asset_Management.triggered.connect(self.Point72_Asset)

        self.actionRenaissance_Technologies = QtWidgets.QAction(MainWindow)
        self.actionRenaissance_Technologies.setObjectName("actionRenaissance_Technologies")
        self.actionRenaissance_Technologies.triggered.connect(self.Renaissance_Technologies)

        self.actionSabby_Management = QtWidgets.QAction(MainWindow)
        self.actionSabby_Management.setObjectName("actionSabby_Management")
        self.actionSabby_Management.triggered.connect(self.Sabby_Management)

        self.actionScion_Asset_Management = QtWidgets.QAction(MainWindow)
        self.actionScion_Asset_Management.setObjectName("actionScion_Asset_Management")
        self.actionScion_Asset_Management.triggered.connect(self.Scion_Asset)

        self.actionStarboad_Value = QtWidgets.QAction(MainWindow)
        self.actionStarboad_Value.setObjectName("actionStarboad_Value")
        self.actionStarboad_Value.triggered.connect(self.Third_Point)

        self.menuOTCBB.addAction(self.actionMost_Active)
        self.menuOTCBB.addAction(self.actionBest_Stock)
        self.menuOTCBB.addAction(self.actionTop_EPS_Stocks)
        self.menuOTCBB.addAction(self.actionLow_EPS_STocks)
        self.menuOTCBB.addAction(self.actionWorst_Stock)
        self.menuOTCBB.addAction(self.actionAMEX_Stocks)
        self.menuOTCBB.addAction(self.actionNYSE_Stocks)
        self.menuOTCBB.addAction(self.actionNASDAQ_Stocks)
        self.menuOTCBB.addAction(self.actionStock_List)
        self.menuFintel.addAction(self.actionBaker_Brothers_Advisors)
        self.menuFintel.addAction(self.actionBaupost_Group)
        self.menuFintel.addAction(self.actionBerkshire_Hathaway)
        self.menuFintel.addAction(self.actionBridgewater_Associates)
        self.menuFintel.addAction(self.actionCascade_Investment)
        self.menuFintel.addAction(self.actionChatham_Asset_Management)
        self.menuFintel.addAction(self.actionDuquesne_Family_Office)
        self.menuFintel.addAction(self.actionGotham_Asset_Management)
        self.menuFintel.addAction(self.actionMangrove_Partners)
        self.menuFintel.addAction(self.actionMelvin_Capital)
        self.menuFintel.addAction(self.actionPerceptive_Advisors)
        self.menuFintel.addAction(self.actionPoint72_Asset_Management)
        self.menuFintel.addAction(self.actionRenaissance_Technologies)
        self.menuFintel.addAction(self.actionSabby_Management)
        self.menuFintel.addAction(self.actionScion_Asset_Management)
        self.menuFintel.addAction(self.actionStarboad_Value)
        self.menubar.addAction(self.menuOTCBB.menuAction())
        self.menubar.addAction(self.menuFintel.menuAction())
        self.menubar.addAction(self.menuFintel_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        ###OTCBB FUNCTION CALLING





    def most_Active_func(self):
            url = "http://otcbbstocks.net/MostActive_Stocks.php"
            self.temp = url
            self.scrapWeb2(url)

        # self.textBrowser.clear()

    def Best_stocks(self):
            url = "http://otcbbstocks.net/top_stocks.php"
            self.temp = url
            self.scrapWeb2(url)

    def Refresh(self):
            self.scrapWeb(self.temp)
            QMessageBox.about(MainWindow, "Message", "Updated!!!")

    def Top_EPS_Stock(self):
            url = "http://otcbbstocks.net/top_eps_stocks.php"
            self.scrapWeb(url)
            self.temp = url

    def WORST_Stock(self):
            url = "http://otcbbstocks.net/worst_stocks.php"
            self.scrapWeb2(url)
            self.temp = url

    def LOW_EPS(self):
            url = "http://otcbbstocks.net/bottom_eps_stocks.php"
            self.scrapWeb(url)
            self.temp = url

    def AMEX_list(self):
            url = "http://marketdatum.com/top_stocks.php"
            self.scrapWeb(url)
            self.temp = url

    def NYSE_Stock(self):
            url = "http://marketdatum.com/top_stocks.php"
            self.scrapWeb(url)
            self.temp = url

    def NASDAQ_Stock(self):
            url = "http://otcbbstocks.net/OTCBB_list.php"
            self.scrapWeb1(url)
            self.temp = url

    def Stock_List1(self):
            url = "http://otcbbstocks.net/OTCBB_list.php"
            self.scrapWeb1(url)
            self.temp = url

####Fintel Menu
    def baker_bros_advisors(self):
             url = "https://fintel.io/i/baker-bros-advisors-lp"
             self.fintel2(url)
             self.temp = url

    def Baupost_Group(self):
             url = "https://fintel.io/i/baupost-group-llc-ma"
             self.fintel2(url)
             self.temp = url

    def Berkshire_Hathaway(self):
             url = "https://fintel.io/i/berkshire-hathaway"
             self.fintel2(url)
             self.temp = url

    def Bridgewater_Associates(self):
             url = "https://fintel.io/i/bridgewater-associates-lp"
             self.fintel1(url)
             self.temp = url

    def Cascade_Investment(self):
             url = "https://fintel.io/i/cascade-investment"
             self.fintel(url)
             self.temp = url

    def Chatham_Asset_Management(self):
             url = "https://fintel.io/i/chatham-asset-management"
             self.fintel(url)
             self.temp = url

    def Duquesne_Family_Office(self):
             url = "https://fintel.io/i/duquesne-family-office-llc"
             self.fintel(url)
             self.temp = url

    def Gotham_Asset_Management(self):
             url = "https://fintel.io/i/gotham-asset-management-llc"
             self.fintel(url)
             self.temp = url

    def Mangrove_Partners(self):
             url = "https://fintel.io/i/mangrove-partners"
             self.fintel(url)
             self.temp = url

    def Melvin_Capital(self):
             url = "https://fintel.io/i/melvin-capital-management-lp"
             self.fintel(url)
             self.temp = url

    def Perceptive_Advisors(self):
             url = "https://fintel.io/i/perceptive-advisors-llc"
             self.fintel(url)
             self.temp = url

    def Point72_Asset(self):
             url = "https://fintel.io/i/point72-asset-management"
             self.fintel(url)
             self.temp = url

    def Renaissance_Technologies(self):
             url = "https://fintel.io/i/renaissance-technologies-llc"
             self.fintel(url)
             self.temp = url

    def Sabby_Management(self):
             url = "https://fintel.io/i/sabby-management-llc"
             self.fintel(url)
             self.temp = url

    def Scion_Asset(self):
             url = "https://fintel.io/i/scion-asset-management-llc"
             self.fintel(url)
             self.temp = url

    def Starboard_Value(self):
             url = "https://fintel.io/i/starboard-value-lp"
             self.fintel(url)
             self.temp = url

    def Third_Point(self):
             url = "https://fintel.io/i/third-point-llc"
             self.fintel(url)
             self.temp = url
    ####OTCBB FOR FUNCTION 1.1


    def scrapWeb1(self, url):
        ##lineedit = self.lineEdit.text()
        ##html = urlopen(lineedit)
        ##bsobj = BeautifulSoup(html, 'lxml')
        lineedit = self.lineEdit.text()
        ##html = urlopen(lineedit)
        ##bsobj = BeautifulSoup(html, 'lxml')
        self.tableWidget.clear()
        data = requests.get(url)
        doc = lh.fromstring(data.content)
        r_elements = doc.xpath('//tr')
        data = []
        count = 0
        for r in r_elements[:]:
            data1 = []
            if count >= 0:
                for i in r:
                    data1.append(str(i.text_content()))
                data.append(data1)
            count = count + 1
        i = 0;
        for var in data:

            for j, var1 in enumerate(var):
                item = QtWidgets.QTableWidgetItem()
                item.setText(var1)
                # self.tableWidget.setItem(n, 0, item)
                #
                # RowCount = self.tableWidget.rowCount()
                self.tableWidget.setItem(i, j, item)
            i = i + 1

    ####otCBB FUNCTION 1.0

    def scrapWeb(self, url):
        ##lineedit = self.lineEdit.text()
        ##html = urlopen(lineedit)
        ##bsobj = BeautifulSoup(html, 'lxml')
        lineedit = self.lineEdit.text()
        ##html = urlopen(lineedit)
        ##bsobj = BeautifulSoup(html, 'lxml')
        self.tableWidget.clear()
        data = requests.get(url)
        doc = lh.fromstring(data.content)
        r_elements = doc.xpath('//tr')
        data = []
        count = 0

        for r in r_elements[:]:
            data1 = []
            if count >= 0:
                for i in r:
                    data1.append(str(i.text_content()))
                data.append(data1)
            count = count + 1
        i = 0;

        final_data = []
        for r in data[4:]:
            # s = str.split(',')
            n_s = r[0].split('(')
            final_str = [n_s[0]] + [n_s[1].replace(')', '')] + r[1:]
            final_data.append(final_str)


            # data1 = []
            # data1.split("(")
            # data1[0]+","+data1[1]
            # if count >= 0:
            #     for i in r:
            #         data1.append(str(i.text_content()))
            #     data.append(data1)
            # count = count + 1
        i = 0
        for var in final_data:

            for j, var1 in enumerate(var):
                item = QtWidgets.QTableWidgetItem()
                item.setText(var1)
                # self.tableWidget.setItem(n, 0, item)
                #
                # RowCount = self.tableWidget.rowCount()
                self.tableWidget.setItem(i, j, item)
            i = i + 1




    def scrapWeb2(self, url):
        ##lineedit = self.lineEdit.text()
        ##html = urlopen(lineedit)
        ##bsobj = BeautifulSoup(html, 'lxml')
        lineedit = self.lineEdit.text()
        ##html = urlopen(lineedit)
        ##bsobj = BeautifulSoup(html, 'lxml')
        self.tableWidget.clear()
        data = requests.get(url)
        doc = lh.fromstring(data.content)
        r_elements = doc.xpath('//tr')
        data = []
        count = 0

        for r in r_elements[:]:
            data1 = []
            if count >= 0:
                for i in r:
                    data1.append(str(i.text_content()))
                data.append(data1)
            count = count + 1
        i = 0;

        final_data = []
        for r in data[1:]:
            # s = str.split(',')
            n_s = r[0].split('(')
            final_str = [n_s[0]] + [n_s[1].replace(')', '')] + r[1:]
            final_data.append(final_str)


            # data1 = []
            # data1.split("(")
            # data1[0]+","+data1[1]
            # if count >= 0:
            #     for i in r:
            #         data1.append(str(i.text_content()))
            #     data.append(data1)
            # count = count + 1
        i = 0
        for var in final_data:

            for j, var1 in enumerate(var):
                item = QtWidgets.QTableWidgetItem()
                item.setText(var1)
                # self.tableWidget.setItem(n, 0, item)
                #
                # RowCount = self.tableWidget.rowCount()
                self.tableWidget.setItem(i, j, item)
            i = i + 1



    ##SCRAPING TARGET URL FUNCTION

    def scrapURL(self):
        lineedit = self.lineEdit.text()
        ##html = urlopen(lineedit)
        ##bsobj = BeautifulSoup(html, 'lxml')
        if lineedit == "":
            QMessageBox.about(MainWindow, "Alert Box", "Please provide a valid url.!!!!")
        else:
            self.temp = lineedit
            self.tableWidget.clear()
            data = requests.get(lineedit)
            doc = lh.fromstring(data.content)
            r_elements = doc.xpath('//tr')
            data = []
            count = 0
            for r in r_elements[:]:
                data1 = []
                if count >= 0:
                    for i in r:
                        data1.append(str(i.text_content()))
                    data.append(data1)
                count = count + 1
            i = 0;
            for var in data:

                for j, var1 in enumerate(var):
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(var1)
                    # self.tableWidget.setItem(n, 0, item)
                    #
                    # RowCount = self.tableWidget.rowCount()
                    self.tableWidget.setItem(i, j, item)
                i = i + 1



    ###Fintel Menu page

    def fintel2(self, url):
        ##lineedit = self.lineEdit.text()
        ##html = urlopen(lineedit)
        ##bsobj = BeautifulSoup(html, 'lxml')
        lineedit = self.lineEdit.text()
        ##html = urlopen(lineedit)
        ##bsobj = BeautifulSoup(html, 'lxml')
        self.tableWidget.clear()
        data = requests.get(url)
        doc = lh.fromstring(data.content)
        r_elements = doc.xpath('//tr')
        data = []
        count = 0
        for r in r_elements[:]:
            data1 = []
            if count >= 0:
                for i in r:
                    data1.append(str(i.text_content()))
                data.append(data1)
            count = count + 1

       # print(data)

        final_data = []
        for r in data[8:-3]:
          #  print('-------', r)
            # s = str.split(',')
            n_s = r[2].split('/')
            if len(n_s) < 2:
                continue
            final_str = r[:2] + [n_s[0]] + [n_s[1].replace(' ', '')] + r[3:]
            final_data.append(final_str)

        i = 0;


        for var in final_data:

            for j, var1 in enumerate(var):
                item = QtWidgets.QTableWidgetItem()
                item.setText(var1)
                # self.tableWidget.setItem(n, 0, item)
                #
                # RowCount = self.tableWidget.rowCount()
                self.tableWidget.setItem(i, j, item)
            i = i + 1

    def fintel1(self, url):
        ##lineedit = self.lineEdit.text()
        ##html = urlopen(lineedit)
        ##bsobj = BeautifulSoup(html, 'lxml')
        lineedit = self.lineEdit.text()
        ##html = urlopen(lineedit)
        ##bsobj = BeautifulSoup(html, 'lxml')
        self.tableWidget.clear()
        data = requests.get(url)
        doc = lh.fromstring(data.content)
        r_elements = doc.xpath('//tr')
        data = []
        count = 0
        for r in r_elements[:]:
            data1 = []
            if count >= 0:
                for i in r:
                    data1.append(str(i.text_content()))
                data.append(data1)
            count = count + 1

        # print(data)

        final_data = []
        for r in data[10:-3]:
            #  print('-------', r)
            # s = str.split(',')
            n_s = r[2].split('/')
            if len(n_s) < 2:
                continue
            final_str = r[:2] + [n_s[0]] + [n_s[1].replace(' ', '')] + r[3:]
            final_data.append(final_str)

        i = 0;

        for var in final_data:

            for j, var1 in enumerate(var):
                item = QtWidgets.QTableWidgetItem()
                item.setText(var1)
                # self.tableWidget.setItem(n, 0, item)
                #
                # RowCount = self.tableWidget.rowCount()
                self.tableWidget.setItem(i, j, item)
            i = i + 1




    def fintel(self, url):
        ##lineedit = self.lineEdit.text()
        ##html = urlopen(lineedit)
        ##bsobj = BeautifulSoup(html, 'lxml')
        lineedit = self.lineEdit.text()
        ##html = urlopen(lineedit)
        ##bsobj = BeautifulSoup(html, 'lxml')
        self.tableWidget.clear()
        data = requests.get(url)
        doc = lh.fromstring(data.content)
        r_elements = doc.xpath('//tr')
        data = []
        count = 0
        for r in r_elements[:]:
            data1 = []
            if count >= 0:
                for i in r:
                    data1.append(str(i.text_content()))
                data.append(data1)
            count = count + 1
        i = 0;
        for var in data:

            for j, var1 in enumerate(var):
                item = QtWidgets.QTableWidgetItem()
                item.setText(var1)
                # self.tableWidget.setItem(n, 0, item)
                #
                # RowCount = self.tableWidget.rowCount()
                self.tableWidget.setItem(i, j, item)
            i = i + 1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Update"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Target URL"))
        self.pushButton.setText(_translate("MainWindow", "Scrap URL"))
        self.menuOTCBB.setTitle(_translate("MainWindow", "OTCBB"))
        self.menuFintel.setTitle(_translate("MainWindow", "Fintel"))
        self.menuFintel_2.setTitle(_translate("MainWindow", "Fintel"))
        self.actionMost_Active.setText(_translate("MainWindow", "Most Active "))
        self.actionBest_Stock.setText(_translate("MainWindow", "Best Stock"))
        self.actionTop_EPS_Stocks.setText(_translate("MainWindow", "Top EPS Stocks"))
        self.actionLow_EPS_STocks.setText(_translate("MainWindow", "Worst EPS Stocks"))
        self.actionLow_EPS_STocks.setText(_translate("MainWindow", "Low EPS STocks"))
        self.actionAMEX_Stocks.setText(_translate("MainWindow", "AMEX Stocks"))
        self.actionNYSE_Stocks.setText(_translate("MainWindow", "NYSE Stocks"))
        self.actionNASDAQ_Stocks.setText(_translate("MainWindow", "NASDAQ Stocks"))
        self.actionStock_List.setText(_translate("MainWindow", "Stock List"))
        self.actionBaker_Brothers_Advisors.setText(_translate("MainWindow", "Baker Brothers Advisors"))
        self.actionBaupost_Group.setText(_translate("MainWindow", "Baupost Group"))
        self.actionBerkshire_Hathaway.setText(_translate("MainWindow", "Berkshire Hathaway"))
        self.actionBridgewater_Associates.setText(_translate("MainWindow", "Bridgewater Associates"))
        self.actionCascade_Investment.setText(_translate("MainWindow", "Cascade Investment"))
        self.actionChatham_Asset_Management.setText(_translate("MainWindow", "Chatham Asset Management"))
        self.actionDuquesne_Family_Office.setText(_translate("MainWindow", "Duquesne Family Office"))
        self.actionGotham_Asset_Management.setText(_translate("MainWindow", "Gotham Asset Management"))
        self.actionMangrove_Partners.setText(_translate("MainWindow", "Mangrove Partners"))
        self.actionMelvin_Capital.setText(_translate("MainWindow", "Melvin Capital"))
        self.actionPerceptive_Advisors.setText(_translate("MainWindow", "Perceptive Advisors"))
        self.actionPoint72_Asset_Management.setText(_translate("MainWindow", "Point72 Asset Management"))
        self.actionRenaissance_Technologies.setText(_translate("MainWindow", "Renaissance Technologies"))
        self.actionSabby_Management.setText(_translate("MainWindow", "Sabby Management"))
        self.actionScion_Asset_Management.setText(_translate("MainWindow", "Scion Asset Management"))
        self.actionStarboad_Value.setText(_translate("MainWindow", "Starboad Value"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

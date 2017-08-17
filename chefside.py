from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from submenu import Ui_Dialog
import pymysql
import functools
import socket
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.creds = []
        self.tempButton=[]
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuActions = QtGui.QMenu(self.menubar)
        self.menuActions.setObjectName(_fromUtf8("menuActions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionConnectdb = QtGui.QAction(MainWindow)
        self.actionConnectdb.setObjectName(_fromUtf8("actionConnectdb"))
        self.actionReload = QtGui.QAction(MainWindow)
        self.actionReload.setObjectName(_fromUtf8("actionReload"))
        self.menuActions.addAction(self.actionConnectdb)
        self.menuActions.addAction(self.actionReload)
        self.menubar.addAction(self.menuActions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionConnectdb, QtCore.SIGNAL("activated()"), self.test)
        QtCore.QObject.connect(self.actionReload, QtCore.SIGNAL(_fromUtf8("activated()")), self.reload)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #submenu
        self.Dialog = QtGui.QDialog()
        d = Ui_Dialog()
        d.setupUi(self.Dialog)
        self.waitingforconnection = waitingforconnection()
        self.waitingforconnection.start()
        QtCore.QObject.connect(self.waitingforconnection, SIGNAL("incoming"), self.reload)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ChefSideUI", None))
        self.menuActions.setTitle(_translate("MainWindow", "Actions", None))
        self.actionConnectdb.setText(_translate("MainWindow", "connectdb", None))
        self.actionReload.setText(_translate("MainWindow", "reload", None))

        notfound = False
        self.creds.insert(2, "")
        try:
            config = open('.dbconfig', 'r').read()
            for i in config.splitlines():
                self.creds.insert(0, i)
            if self.creds[2] != "":
                self.creds[2], self.creds[0] = self.creds[0], self.creds[2]
                self.creds[1], self.creds[0] = self.creds[0], self.creds[1]
        except FileNotFoundError:
            notfound = True

        if (notfound):
            self.statusbar.setStyleSheet("color:red")
            self.statusbar.showMessage("NO DATABASE SETTINGS FOUND!", 100000000)

        else:
            self.con = pymysql.connect(host=self.creds[1], user=self.creds[0], passwd=self.creds[2],
                                  db='ultimate_drive_thru')
            try:
                self.con
            except NameError:
                self.statusbar.showMessage("Umm", 100000000)
            else:
                a = self.con.cursor()
                a.execute("select Tid,item,qty,comments from orders where is_served='0'")
                orders = a.fetchall()

                for i in reversed(range(self.tableWidget.rowCount())):
                    self.tableWidget.removeRow(i)#Clear before put

                self.tableWidget.setColumnCount(4)
                for rownum,rowdata in enumerate(orders):
                    rowdata=list(rowdata)
                    self.tableWidget.insertRow(rownum)
                    self.tempButton += [QtGui.QPushButton("served!")]

                    QtCore.QObject.connect(self.tempButton[rownum], QtCore.SIGNAL(_fromUtf8("clicked()")),functools.partial(self.deletefromdb,rowdata[0],rownum))

                    rowdata.pop(0)
                    rowdata=tuple(rowdata)
                    self.tableWidget.setCellWidget(rownum,3,self.tempButton[rownum])


                    for colnum,coldata in enumerate(rowdata):
                        self.tableWidget.setItem(rownum, colnum, QtGui.QTableWidgetItem(str(coldata)))

                self.tableWidget.setHorizontalHeaderLabels(['Item', 'Quantity', 'Comments', 'Actions'])

    def deletefromdb(self,*args):
        b = self.con.cursor()
        #b.execute('select Tid,item,qty,comments from orders')
        query="update orders set is_served='1' where Tid={}".format(args[0])
        print(query)
        print(type(query))
        b.execute(query)
        self.con.commit()
        self.tableWidget.removeRow(args[1])

    def test(self):
        self.Dialog.show()

    def reload(self):
        #working on it
        self.tempButton=[]
        self.creds.clear()
        self.retranslateUi(MainWindow)

class waitingforconnection(QThread):
    def __init__(self,parent=None):
        super(waitingforconnection,self).__init__(parent)
    def run(self):
        s = socket.socket()
        host = "localhost"
        port = 12345
        s.bind((host, port))

        s.listen(5)
        while True:
            c, addr = s.accept()
            print('Got connection from', addr)
            c.send('Thank you for connecting'.encode(encoding='utf-8'))
            c.close()
        #if conncted==TRUE
            self.emit(SIGNAL("incoming"))
        #do that ^


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

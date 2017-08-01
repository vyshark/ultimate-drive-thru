from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from takeorder import takeorderfunction
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
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(744, 414)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout = QtGui.QGridLayout(self.page)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_Burgers = QtGui.QVBoxLayout()
        self.verticalLayout_Burgers.setObjectName(_fromUtf8("verticalLayout_Burgers"))
        self.label_Burgers = QtGui.QLabel(self.page)
        self.label_Burgers.setObjectName(_fromUtf8("label_Burgers"))
        self.verticalLayout_Burgers.addWidget(self.label_Burgers)
        self.tableWidget_Burgers = QtGui.QTableWidget(self.page)
        self.tableWidget_Burgers.setAlternatingRowColors(True)
        self.tableWidget_Burgers.setColumnCount(2)
        self.tableWidget_Burgers.setObjectName(_fromUtf8("tableWidget_Burgers"))
        self.tableWidget_Burgers.setRowCount(0)
        self.verticalLayout_Burgers.addWidget(self.tableWidget_Burgers)
        self.gridLayout.addLayout(self.verticalLayout_Burgers, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.page_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.tableWidget = QtGui.QTableWidget(self.page_2)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Desktop/speaker.gif")))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.orderherestatic = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orderherestatic.sizePolicy().hasHeightForWidth())
        self.orderherestatic.setSizePolicy(sizePolicy)
        self.orderherestatic.setObjectName(_fromUtf8("orderherestatic"))
        self.verticalLayout.addWidget(self.orderherestatic)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Desktop/speak.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 744, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuActions = QtGui.QMenu(self.menubar)
        self.menuActions.setObjectName(_fromUtf8("menuActions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionDatabase_Config = QtGui.QAction(MainWindow)
        self.actionDatabase_Config.setObjectName(_fromUtf8("actionDatabase_Config"))
        self.menuActions.addAction(self.actionDatabase_Config)
        self.menubar.addAction(self.menuActions.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.calltakeorder)   #BUTTON CLICK ACTION
        self.logicthread=logicthread()                                                                       #INITIATING THREAD
        self.connect(self.logicthread,SIGNAL("logicthreaddone(QString)"),self.logicthreaddone,Qt.DirectConnection)  #Connecting to Custom Signal->Slot
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_Burgers.setText(_translate("MainWindow", "<center><font color=\"purple\" size=\"5\"><b>Burgers<b></font></center>", None))
        self.label_2.setText(_translate("MainWindow", "<center><font color=\"purple\" size=\"5\"><b>Drinks<b></font></center>", None))
        self.orderherestatic.setText(_translate("MainWindow", "<center><font color=\"red\" size=\"10\"><b>ORDER HERE<b></font></center>", None))
        self.pushButton.setText(_translate("MainWindow", "Place Order", None))
        self.menuActions.setTitle(_translate("MainWindow", "Actions", None))
        self.actionDatabase_Config.setText(_translate("MainWindow", "Database Config", None))

    def calltakeorder(self):
        self.logicthread.start()
        self.statusbar.showMessage("hello, what would you like to eat?",5000)
        self.pushButton.setDisabled()

    def logicthreaddone(self,message):
        self.pushButton.setEnabled()
        self.statusbar.showMessage(message,5000)

class logicthread(QThread):
    def __init__(self,parent=None):
        super(logicthread,self).__init__(parent)
    def run(self):
        message=takeorderfunction()
        self.emit(SIGNAL("logicthreaddone(QString)"),message)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


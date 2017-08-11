from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import takeorder
from submenu import Ui_Dialog
from receipt import Ui_receiptDialog
import pymysql

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
    creds=[]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(744, 469)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./icons/mcdonalds.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 446, 411))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.menu = QtGui.QTextBrowser(self.scrollAreaWidgetContents)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.verticalLayout_2.addWidget(self.menu)
        self.messagebox = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.messagebox.setMinimumSize(QtCore.QSize(0, 0))
        self.messagebox.setMaximumSize(QtCore.QSize(16777215, 55))
        self.messagebox.setReadOnly(True)
        self.messagebox.setObjectName(_fromUtf8("messagebox"))
        self.verticalLayout_2.addWidget(self.messagebox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("./icons/speaker.gif")))
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
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./icons/speak.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("./icons/action-db-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionDatabase_Config.setIcon(icon2)
        self.actionDatabase_Config.setObjectName(_fromUtf8("actionDatabase_Config"))
        self.actionRestart = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("./icons/restart.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionRestart.setIcon(icon3)
        self.actionRestart.setObjectName(_fromUtf8("actionRestart"))
        self.menuActions.addAction(self.actionDatabase_Config)
        self.menuActions.addAction(self.actionRestart)
        self.menubar.addAction(self.menuActions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.calltakeorder)   #BUTTON CLICK ACTION
        QtCore.QObject.connect(self.actionDatabase_Config,QtCore.SIGNAL("activated()"),self.test)
        self.logicthread=logicthread()  
        QtCore.QObject.connect(self.actionRestart, QtCore.SIGNAL(_fromUtf8("activated()")), self.reload)                                                                     #INITIATING THREAD
        QtCore.QObject.connect(self.logicthread,SIGNAL("logicthreaddone"),self.logicthreaddone)  #Connecting to Custom Signal->Slot
        QtCore.QObject.connect(self.logicthread, SIGNAL("logicthreadreceipt"), self.logicthreadreceipt)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #submenu
        self.Dialog = QtGui.QDialog()
        d = Ui_Dialog()
        d.setupUi(self.Dialog)

        #receipt

        self.receipt=QtGui.QDialog()
        self.r = Ui_receiptDialog()



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

        notfound = False
        #self.creds = []
        self.creds.insert(2,"")
        try:
            config = open('.dbconfig', 'r').read()
            for i in config.splitlines():
                self.creds.insert(0,i)
            if self.creds[2] != "":
                self.creds[2], self.creds[0] = self.creds[0], self.creds[2]
                self.creds[1], self.creds[0] = self.creds[0], self.creds[1]
        except FileNotFoundError:
            notfound = True

        if(notfound):
            self.statusbar.setStyleSheet("color:red")
            self.statusbar.showMessage("NO DATABASE SETTINGS FOUND!",100000000)
            self.pushButton.setEnabled(False)
            self.messagebox.setText("Go to Action>Database Config> and enter your database credentials and restart")
        else:
            con = pymysql.connect(host=self.creds[1], user=self.creds[0], passwd=self.creds[2], db='ultimate_drive_thru')
            try:
                con
            except NameError:
                self.messagebox.setText("ummmmm...")
            else:
                a=con.cursor()
                a.execute('select * from type')
                types = a.fetchall()
                a.execute('select typeid,item,price from Menu')
                menu = a.fetchall()
                answer = '<section class="menu-panel"><p class="adorn-brdr-btm menu-time">...............</p><h3>Our Menu</h3><p class="intro">...............</p>'
                for i, j in types:
                    answer += '<h4><span>' + j + '</span></h4>'
                    for a, b, c in menu:
                        if i == a:
                            answer += '<ul class="menu-items"><li><strong>'
                            answer += b.ljust(50, '_') + " " + c + "</strong></li></ul>"
                    answer += "...</section>"
                themenu=answer




            self.menu.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+
                           themenu
                                     +"</p></body></html>", None))
            self.messagebox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Messagebox initial</p></body></html>", None))
        self.orderherestatic.setText(_translate("MainWindow", "<center><font color=\"red\" size=\"10\"><b>ORDER HERE<b></font></center>", None))
        self.pushButton.setText(_translate("MainWindow", "Place Order", None))
        self.menuActions.setTitle(_translate("MainWindow", "Actions", None))
        self.actionDatabase_Config.setText(_translate("MainWindow", "Database Config", None))
        self.actionRestart.setText(_translate("MainWindow", "Restart", None))

    def calltakeorder(self):

        self.logicthread.start()

        self.statusbar.setStyleSheet("color:blue")
        self.statusbar.showMessage("hello, what would you like to eat?",5000)
        self.pushButton.setEnabled(False)

    def reload(self):
        #working on it
        self.retranslateUi(MainWindow)
        self.pushButton.setEnabled(True)


    def logicthreaddone(self,message):
        self.pushButton.setEnabled(True)
        print(message)
        self.messagebox.setText(message)

    def logicthreadreceipt(self,message):
        self.r.setupUi(self.receipt,message,self.creds)
        self.receipt.show()


    def test(self):
        self.Dialog.show()

class logicthread(QThread):
    def __init__(self,parent=None):
        super(logicthread,self).__init__(parent)
    def run(self):
        #message=""
        finalod, mess, name=takeorder.takeorderfunction()
        #message=message.split('%%')
        self.emit(SIGNAL("logicthreaddone"), str(finalod))

        message=takeorder.confirmorder(finalod, mess, name)
        message=message.split('%%')
        self.emit(SIGNAL("logicthreadreceipt"), message[1])



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./icons/mcdonalds.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_Host = QtGui.QLabel(Dialog)
        self.label_Host.setObjectName(_fromUtf8("label_Host"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_Host)
        self.line_Host = QtGui.QLineEdit(Dialog)
        self.line_Host.setObjectName(_fromUtf8("line_Host"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.line_Host)
        self.label_User = QtGui.QLabel(Dialog)
        self.label_User.setObjectName(_fromUtf8("label_User"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_User)
        self.line_User = QtGui.QLineEdit(Dialog)
        self.line_User.setObjectName(_fromUtf8("line_User"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.line_User)
        self.label_password = QtGui.QLabel(Dialog)
        self.label_password.setObjectName(_fromUtf8("label_password"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_password)
        self.line_Password = QtGui.QLineEdit(Dialog)
        self.line_Password.setInputMask(_fromUtf8(""))
        self.line_Password.setEchoMode(QtGui.QLineEdit.Password)
        self.line_Password.setObjectName(_fromUtf8("line_Password"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.line_Password)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtGui.QFormLayout.FieldRole, spacerItem)
        self.dbstatus = QtGui.QLabel(Dialog)
        self.dbstatus.setText(_fromUtf8(""))
        self.dbstatus.setObjectName(_fromUtf8("dbstatus"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.dbstatus)
        self.horizontalLayout.addLayout(self.formLayout)
        self.label = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("./icons/database.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), lambda :self.beforeaccept(Dialog))
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.thetext=[]
        self.thetext.insert(2,"")
        try:
            config = open('.dbconfig.bak', 'r').read()
            for i in config.splitlines():
                self.thetext.insert(0,i)
            if self.thetext[2] != "":
                self.thetext[2], self.thetext[0] = self.thetext[0], self.thetext[2]
                self.thetext[1], self.thetext[0] = self.thetext[0], self.thetext[1]
        except Exception as e:
            print("laterz")

        else:
            self.line_Host.setText(self.thetext[1])
            self.line_User.setText(self.thetext[0])
            self.line_Password.setText(self.thetext[2])

        Dialog.setWindowTitle(_translate("Dialog", "Connect Restaurant DB", None))
        self.label_Host.setText(_translate("Dialog", "Host", None))
        self.label_User.setText(_translate("Dialog", "User", None))
        self.label_password.setText(_translate("Dialog", "password", None))

    def beforeaccept(self,Dialog):
        errormessage=""
        try:
            con=pymysql.connect(host=self.line_Host.text(),user=self.line_User.text(),password=self.line_Password.text(),db='ultimate_drive_thru')
        except pymysql.err.OperationalError:
            errormessage+="Check your credentials."
            self.dbstatus.setText("<font color='red'>"+errormessage+"<font>")

        try:
            con
        except NameError:
            errormessage+="<br>Failed to Connect!"
            self.dbstatus.setText("<font color='red'>"+errormessage+"<font>")
        else:
            try:
                f=open('.dbconfig','w')
                f.write(self.line_Host.text()+"\n"+self.line_User.text()+"\n"+self.line_Password.text())
                self.dbstatus.setText("<font color='green'>Sucessfully Connected!<font>")
                
            except:
                self.dbstatus.setText("<font color='red'>Could not write to disk.<font>")

            Dialog.accept()




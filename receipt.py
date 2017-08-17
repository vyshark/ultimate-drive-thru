from PyQt4 import QtCore, QtGui
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

class Ui_receiptDialog(object):

    def setupUi(self, receiptDialog,TID,creds):
        self.TID=TID
        self.creds=creds
        receiptDialog.setObjectName(_fromUtf8("receiptDialog"))
        receiptDialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("clones/ultimate-drive-thru/icons/mcdonalds.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        receiptDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(receiptDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.receipttext = QtGui.QTextBrowser(receiptDialog)
        self.receipttext.setObjectName(_fromUtf8("receipttext"))
        self.verticalLayout.addWidget(self.receipttext)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.accept = QtGui.QPushButton(receiptDialog)
        self.accept.setObjectName(_fromUtf8("accept"))
        self.horizontalLayout.addWidget(self.accept)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(receiptDialog)
        QtCore.QObject.connect(self.accept, QtCore.SIGNAL(_fromUtf8("clicked()")), receiptDialog.close)
        QtCore.QMetaObject.connectSlotsByName(receiptDialog)

    def retranslateUi(self, receiptDialog):
        total=0
        x=""
        print("TID",self.TID)
        transaction=self.TID

        receiptDialog.setWindowTitle(_translate("receiptDialog", "Receipt", None))
        self.accept.setText(_translate("receiptDialog", "OK", None))

        con = pymysql.connect(host=self.creds[1], user=self.creds[0], passwd=self.creds[2], db='ultimate_drive_thru')

        cur=con.cursor()
        cur.execute("select * from orders where Tid=%s", transaction)
        finalreceipt=cur.fetchall()
        head="ORDER ID:"+ str(transaction)
        for i in finalreceipt:
            x=x+str(i[2])+" X"+str(i[1])+" ......... "+ str(i[4])+"\n"
            total=total+int(i[4])
        final=head+"\n\n\n"+x+"\n\n\nTOTAL:"+str(total)
        self.receipttext.setText(final)


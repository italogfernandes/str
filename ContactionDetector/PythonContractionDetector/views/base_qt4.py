# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.resize(735, 538)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(597, 538))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayoutOptions = QtGui.QVBoxLayout()
        self.verticalLayoutOptions.setObjectName(_fromUtf8("verticalLayoutOptions"))
        self.lbl_options = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_options.sizePolicy().hasHeightForWidth())
        self.lbl_options.setSizePolicy(sizePolicy)
        self.lbl_options.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lbl_options.setObjectName(_fromUtf8("lbl_options"))
        self.verticalLayoutOptions.addWidget(self.lbl_options)
        self.horizontalLayoutBtns = QtGui.QHBoxLayout()
        self.horizontalLayoutBtns.setObjectName(_fromUtf8("horizontalLayoutBtns"))
        spacerItem = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutBtns.addItem(spacerItem)
        self.verticalLayoutBtns = QtGui.QVBoxLayout()
        self.verticalLayoutBtns.setObjectName(_fromUtf8("verticalLayoutBtns"))
        self.btn_start = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.verticalLayoutBtns.addWidget(self.btn_start)
        self.btn_calib = QtGui.QPushButton(self.centralwidget)
        self.btn_calib.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_calib.setObjectName(_fromUtf8("btn_calib"))
        self.verticalLayoutBtns.addWidget(self.btn_calib)
        self.horizontalLayoutBtns.addLayout(self.verticalLayoutBtns)
        spacerItem1 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutBtns.addItem(spacerItem1)
        self.verticalLayoutOptions.addLayout(self.horizontalLayoutBtns)
        self.verticalLayoutThreshould = QtGui.QVBoxLayout()
        self.verticalLayoutThreshould.setObjectName(_fromUtf8("verticalLayoutThreshould"))
        self.lbl_threshould = QtGui.QLabel(self.centralwidget)
        self.lbl_threshould.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_threshould.setObjectName(_fromUtf8("lbl_threshould"))
        self.verticalLayoutThreshould.addWidget(self.lbl_threshould)
        self.horizontalLayoutThreshould = QtGui.QHBoxLayout()
        self.horizontalLayoutThreshould.setObjectName(_fromUtf8("horizontalLayoutThreshould"))
        spacerItem2 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutThreshould.addItem(spacerItem2)
        self.sl_threshould = QtGui.QSlider(self.centralwidget)
        self.sl_threshould.setOrientation(QtCore.Qt.Vertical)
        self.sl_threshould.setObjectName(_fromUtf8("sl_threshould"))
        self.horizontalLayoutThreshould.addWidget(self.sl_threshould)
        spacerItem3 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutThreshould.addItem(spacerItem3)
        self.verticalLayoutThreshould.addLayout(self.horizontalLayoutThreshould)
        self.verticalLayoutCheckBoxes = QtGui.QVBoxLayout()
        self.verticalLayoutCheckBoxes.setObjectName(_fromUtf8("verticalLayoutCheckBoxes"))
        self.cb_emg = QtGui.QCheckBox(self.centralwidget)
        self.cb_emg.setObjectName(_fromUtf8("cb_emg"))
        self.verticalLayoutCheckBoxes.addWidget(self.cb_emg)
        self.cb_hbt = QtGui.QCheckBox(self.centralwidget)
        self.cb_hbt.setObjectName(_fromUtf8("cb_hbt"))
        self.verticalLayoutCheckBoxes.addWidget(self.cb_hbt)
        self.cb_ret = QtGui.QCheckBox(self.centralwidget)
        self.cb_ret.setObjectName(_fromUtf8("cb_ret"))
        self.verticalLayoutCheckBoxes.addWidget(self.cb_ret)
        self.cb_env = QtGui.QCheckBox(self.centralwidget)
        self.cb_env.setObjectName(_fromUtf8("cb_env"))
        self.verticalLayoutCheckBoxes.addWidget(self.cb_env)
        self.cb_lim = QtGui.QCheckBox(self.centralwidget)
        self.cb_lim.setObjectName(_fromUtf8("cb_lim"))
        self.verticalLayoutCheckBoxes.addWidget(self.cb_lim)
        self.cb_det = QtGui.QCheckBox(self.centralwidget)
        self.cb_det.setObjectName(_fromUtf8("cb_det"))
        self.verticalLayoutCheckBoxes.addWidget(self.cb_det)
        self.verticalLayoutThreshould.addLayout(self.verticalLayoutCheckBoxes)
        self.verticalLayoutOptions.addLayout(self.verticalLayoutThreshould)
        self.horizontalLayout.addLayout(self.verticalLayoutOptions)
        self.verticalLayoutGraphStatus = QtGui.QVBoxLayout()
        self.verticalLayoutGraphStatus.setObjectName(_fromUtf8("verticalLayoutGraphStatus"))
        self.verticalLayoutGraph = QtGui.QVBoxLayout()
        self.verticalLayoutGraph.setObjectName(_fromUtf8("verticalLayoutGraph"))
        self.label_replace = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_replace.sizePolicy().hasHeightForWidth())
        self.label_replace.setSizePolicy(sizePolicy)
        self.label_replace.setObjectName(_fromUtf8("label_replace"))
        self.verticalLayoutGraph.addWidget(self.label_replace)
        self.verticalLayoutGraphStatus.addLayout(self.verticalLayoutGraph)
        self.lbl_status = QtGui.QLabel(self.centralwidget)
        self.lbl_status.setObjectName(_fromUtf8("lbl_status"))
        self.verticalLayoutGraphStatus.addWidget(self.lbl_status)
        self.horizontalLayout.addLayout(self.verticalLayoutGraphStatus)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Contraction Detector", None))
        self.lbl_options.setText(_translate("MainWindow", "Opções:", None))
        self.btn_start.setToolTip(_translate("MainWindow", "Start", None))
        self.btn_start.setText(_translate("MainWindow", "S", None))
        self.btn_calib.setToolTip(_translate("MainWindow", "Calibrar", None))
        self.btn_calib.setText(_translate("MainWindow", "C", None))
        self.lbl_threshould.setText(_translate("MainWindow", "Limiar:", None))
        self.cb_emg.setText(_translate("MainWindow", "EMG", None))
        self.cb_hbt.setText(_translate("MainWindow", "HBT", None))
        self.cb_ret.setText(_translate("MainWindow", "RET", None))
        self.cb_env.setText(_translate("MainWindow", "ENV", None))
        self.cb_lim.setText(_translate("MainWindow", "LIM", None))
        self.cb_det.setText(_translate("MainWindow", "DET", None))
        self.label_replace.setText(_translate("MainWindow", "Here will be the chart", None))
        self.lbl_status.setText(_translate("MainWindow", "Status:", None))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))

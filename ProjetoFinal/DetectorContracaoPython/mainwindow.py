# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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
        MainWindow.resize(680, 442)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEditEnqueue = QtGui.QLineEdit(self.tab)
        self.lineEditEnqueue.setObjectName(_fromUtf8("lineEditEnqueue"))
        self.horizontalLayout_4.addWidget(self.lineEditEnqueue)
        self.btnEnqueue = QtGui.QPushButton(self.tab)
        self.btnEnqueue.setObjectName(_fromUtf8("btnEnqueue"))
        self.horizontalLayout_4.addWidget(self.btnEnqueue)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.lineEditDequeue = QtGui.QLineEdit(self.tab)
        self.lineEditDequeue.setObjectName(_fromUtf8("lineEditDequeue"))
        self.horizontalLayout_6.addWidget(self.lineEditDequeue)
        self.btnDequeue = QtGui.QPushButton(self.tab)
        self.btnDequeue.setObjectName(_fromUtf8("btnDequeue"))
        self.horizontalLayout_6.addWidget(self.btnDequeue)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.btnClear = QtGui.QPushButton(self.tab)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.verticalLayout_3.addWidget(self.btnClear)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.lblStatus = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblStatus.sizePolicy().hasHeightForWidth())
        self.lblStatus.setSizePolicy(sizePolicy)
        self.lblStatus.setMinimumSize(QtCore.QSize(300, 0))
        self.lblStatus.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        self.horizontalLayout_3.addWidget(self.lblStatus)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_11 = QtGui.QWidget()
        self.tab_11.setObjectName(_fromUtf8("tab_11"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.tab_11)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.label_10 = QtGui.QLabel(self.tab_11)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_12.addWidget(self.label_10)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.lineEditEnqueue_3 = QtGui.QLineEdit(self.tab_11)
        self.lineEditEnqueue_3.setObjectName(_fromUtf8("lineEditEnqueue_3"))
        self.horizontalLayout_15.addWidget(self.lineEditEnqueue_3)
        self.btnEnqueue_3 = QtGui.QPushButton(self.tab_11)
        self.btnEnqueue_3.setObjectName(_fromUtf8("btnEnqueue_3"))
        self.horizontalLayout_15.addWidget(self.btnEnqueue_3)
        self.verticalLayout_12.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.lineEditDequeue_3 = QtGui.QLineEdit(self.tab_11)
        self.lineEditDequeue_3.setObjectName(_fromUtf8("lineEditDequeue_3"))
        self.horizontalLayout_16.addWidget(self.lineEditDequeue_3)
        self.btnDequeue_3 = QtGui.QPushButton(self.tab_11)
        self.btnDequeue_3.setObjectName(_fromUtf8("btnDequeue_3"))
        self.horizontalLayout_16.addWidget(self.btnDequeue_3)
        self.verticalLayout_12.addLayout(self.horizontalLayout_16)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem1)
        self.btnClear_3 = QtGui.QPushButton(self.tab_11)
        self.btnClear_3.setObjectName(_fromUtf8("btnClear_3"))
        self.verticalLayout_12.addWidget(self.btnClear_3)
        self.horizontalLayout_17.addLayout(self.verticalLayout_12)
        self.lblStatus_3 = QtGui.QLabel(self.tab_11)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblStatus_3.sizePolicy().hasHeightForWidth())
        self.lblStatus_3.setSizePolicy(sizePolicy)
        self.lblStatus_3.setMinimumSize(QtCore.QSize(300, 0))
        self.lblStatus_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblStatus_3.setObjectName(_fromUtf8("lblStatus_3"))
        self.horizontalLayout_17.addWidget(self.lblStatus_3)
        self.tabWidget.addTab(self.tab_11, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.btnStartThr = QtGui.QPushButton(self.tab_2)
        self.btnStartThr.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnStartThr.setObjectName(_fromUtf8("btnStartThr"))
        self.verticalLayout_4.addWidget(self.btnStartThr)
        self.btnPauseThr = QtGui.QPushButton(self.tab_2)
        self.btnPauseThr.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnPauseThr.setObjectName(_fromUtf8("btnPauseThr"))
        self.verticalLayout_4.addWidget(self.btnPauseThr)
        self.btnResumeThr = QtGui.QPushButton(self.tab_2)
        self.btnResumeThr.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnResumeThr.setObjectName(_fromUtf8("btnResumeThr"))
        self.verticalLayout_4.addWidget(self.btnResumeThr)
        self.btnStopThr = QtGui.QPushButton(self.tab_2)
        self.btnStopThr.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnStopThr.setObjectName(_fromUtf8("btnStopThr"))
        self.verticalLayout_4.addWidget(self.btnStopThr)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.editResultThr = QtGui.QPlainTextEdit(self.tab_2)
        self.editResultThr.setObjectName(_fromUtf8("editResultThr"))
        self.horizontalLayout_8.addWidget(self.editResultThr)
        self.lblResultThr = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblResultThr.sizePolicy().hasHeightForWidth())
        self.lblResultThr.setSizePolicy(sizePolicy)
        self.lblResultThr.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblResultThr.setObjectName(_fromUtf8("lblResultThr"))
        self.horizontalLayout_8.addWidget(self.lblResultThr)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_12 = QtGui.QWidget()
        self.tab_12.setObjectName(_fromUtf8("tab_12"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout(self.tab_12)
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.label_11 = QtGui.QLabel(self.tab_12)
        self.label_11.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_13.addWidget(self.label_11)
        self.btnStartThr_4 = QtGui.QPushButton(self.tab_12)
        self.btnStartThr_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnStartThr_4.setObjectName(_fromUtf8("btnStartThr_4"))
        self.verticalLayout_13.addWidget(self.btnStartThr_4)
        self.btnPauseThr_4 = QtGui.QPushButton(self.tab_12)
        self.btnPauseThr_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnPauseThr_4.setObjectName(_fromUtf8("btnPauseThr_4"))
        self.verticalLayout_13.addWidget(self.btnPauseThr_4)
        self.btnResumeThr_4 = QtGui.QPushButton(self.tab_12)
        self.btnResumeThr_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnResumeThr_4.setObjectName(_fromUtf8("btnResumeThr_4"))
        self.verticalLayout_13.addWidget(self.btnResumeThr_4)
        self.btnStopThr_4 = QtGui.QPushButton(self.tab_12)
        self.btnStopThr_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnStopThr_4.setObjectName(_fromUtf8("btnStopThr_4"))
        self.verticalLayout_13.addWidget(self.btnStopThr_4)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem3)
        self.horizontalLayout_19.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.label_12 = QtGui.QLabel(self.tab_12)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_14.addWidget(self.label_12)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.editResultThr_3 = QtGui.QPlainTextEdit(self.tab_12)
        self.editResultThr_3.setObjectName(_fromUtf8("editResultThr_3"))
        self.horizontalLayout_18.addWidget(self.editResultThr_3)
        self.lblResultThr_3 = QtGui.QLabel(self.tab_12)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblResultThr_3.sizePolicy().hasHeightForWidth())
        self.lblResultThr_3.setSizePolicy(sizePolicy)
        self.lblResultThr_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblResultThr_3.setObjectName(_fromUtf8("lblResultThr_3"))
        self.horizontalLayout_18.addWidget(self.lblResultThr_3)
        self.verticalLayout_14.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19.addLayout(self.verticalLayout_14)
        self.tabWidget.addTab(self.tab_12, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_4)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_8 = QtGui.QLabel(self.tab_4)
        self.label_8.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_10.addWidget(self.label_8)
        self.btnStartAcq = QtGui.QPushButton(self.tab_4)
        self.btnStartAcq.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnStartAcq.setObjectName(_fromUtf8("btnStartAcq"))
        self.verticalLayout_10.addWidget(self.btnStartAcq)
        self.btnPauseConsumer = QtGui.QPushButton(self.tab_4)
        self.btnPauseConsumer.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnPauseConsumer.setObjectName(_fromUtf8("btnPauseConsumer"))
        self.verticalLayout_10.addWidget(self.btnPauseConsumer)
        self.btnResumeConsumer = QtGui.QPushButton(self.tab_4)
        self.btnResumeConsumer.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnResumeConsumer.setObjectName(_fromUtf8("btnResumeConsumer"))
        self.verticalLayout_10.addWidget(self.btnResumeConsumer)
        self.btnStopAcq = QtGui.QPushButton(self.tab_4)
        self.btnStopAcq.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnStopAcq.setObjectName(_fromUtf8("btnStopAcq"))
        self.verticalLayout_10.addWidget(self.btnStopAcq)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.label_9 = QtGui.QLabel(self.tab_4)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_11.addWidget(self.label_9)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.editResultAcq = QtGui.QPlainTextEdit(self.tab_4)
        self.editResultAcq.setObjectName(_fromUtf8("editResultAcq"))
        self.horizontalLayout_13.addWidget(self.editResultAcq)
        self.lblResultAcq = QtGui.QLabel(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblResultAcq.sizePolicy().hasHeightForWidth())
        self.lblResultAcq.setSizePolicy(sizePolicy)
        self.lblResultAcq.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblResultAcq.setObjectName(_fromUtf8("lblResultAcq"))
        self.horizontalLayout_13.addWidget(self.lblResultAcq)
        self.verticalLayout_11.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblChartHereMatplotlib = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblChartHereMatplotlib.sizePolicy().hasHeightForWidth())
        self.lblChartHereMatplotlib.setSizePolicy(sizePolicy)
        self.lblChartHereMatplotlib.setAlignment(QtCore.Qt.AlignCenter)
        self.lblChartHereMatplotlib.setObjectName(_fromUtf8("lblChartHereMatplotlib"))
        self.verticalLayout.addWidget(self.lblChartHereMatplotlib)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.btnAddRandomToChart = QtGui.QPushButton(self.tab_3)
        self.btnAddRandomToChart.setObjectName(_fromUtf8("btnAddRandomToChart"))
        self.horizontalLayout_14.addWidget(self.btnAddRandomToChart)
        self.btnAddSinToChart = QtGui.QPushButton(self.tab_3)
        self.btnAddSinToChart.setObjectName(_fromUtf8("btnAddSinToChart"))
        self.horizontalLayout_14.addWidget(self.btnAddSinToChart)
        self.btnClearChart = QtGui.QPushButton(self.tab_3)
        self.btnClearChart.setObjectName(_fromUtf8("btnClearChart"))
        self.horizontalLayout_14.addWidget(self.btnClearChart)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.lblStatusChart = QtGui.QLabel(self.tab_3)
        self.lblStatusChart.setObjectName(_fromUtf8("lblStatusChart"))
        self.verticalLayout.addWidget(self.lblStatusChart)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_13 = QtGui.QWidget()
        self.tab_13.setObjectName(_fromUtf8("tab_13"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.tab_13)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.lblChartHerePyQTGraph = QtGui.QLabel(self.tab_13)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblChartHerePyQTGraph.sizePolicy().hasHeightForWidth())
        self.lblChartHerePyQTGraph.setSizePolicy(sizePolicy)
        self.lblChartHerePyQTGraph.setAlignment(QtCore.Qt.AlignCenter)
        self.lblChartHerePyQTGraph.setObjectName(_fromUtf8("lblChartHerePyQTGraph"))
        self.verticalLayout_15.addWidget(self.lblChartHerePyQTGraph)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.btnAddRandomToChart_2 = QtGui.QPushButton(self.tab_13)
        self.btnAddRandomToChart_2.setObjectName(_fromUtf8("btnAddRandomToChart_2"))
        self.horizontalLayout_20.addWidget(self.btnAddRandomToChart_2)
        self.btnAddSinToChart_2 = QtGui.QPushButton(self.tab_13)
        self.btnAddSinToChart_2.setObjectName(_fromUtf8("btnAddSinToChart_2"))
        self.horizontalLayout_20.addWidget(self.btnAddSinToChart_2)
        self.btnClearChart_2 = QtGui.QPushButton(self.tab_13)
        self.btnClearChart_2.setObjectName(_fromUtf8("btnClearChart_2"))
        self.horizontalLayout_20.addWidget(self.btnClearChart_2)
        self.verticalLayout_15.addLayout(self.horizontalLayout_20)
        self.lblStatusChart_2 = QtGui.QLabel(self.tab_13)
        self.lblStatusChart_2.setObjectName(_fromUtf8("lblStatusChart_2"))
        self.verticalLayout_15.addWidget(self.lblStatusChart_2)
        self.tabWidget.addTab(self.tab_13, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.horizontalLayout_22 = QtGui.QHBoxLayout(self.tab_5)
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.label_13 = QtGui.QLabel(self.tab_5)
        self.label_13.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_16.addWidget(self.label_13)
        self.btnStartAcq_2 = QtGui.QPushButton(self.tab_5)
        self.btnStartAcq_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnStartAcq_2.setObjectName(_fromUtf8("btnStartAcq_2"))
        self.verticalLayout_16.addWidget(self.btnStartAcq_2)
        self.btnPauseConsumer_2 = QtGui.QPushButton(self.tab_5)
        self.btnPauseConsumer_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnPauseConsumer_2.setObjectName(_fromUtf8("btnPauseConsumer_2"))
        self.verticalLayout_16.addWidget(self.btnPauseConsumer_2)
        self.btnResumeConsumer_2 = QtGui.QPushButton(self.tab_5)
        self.btnResumeConsumer_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnResumeConsumer_2.setObjectName(_fromUtf8("btnResumeConsumer_2"))
        self.verticalLayout_16.addWidget(self.btnResumeConsumer_2)
        self.btnStopAcq_2 = QtGui.QPushButton(self.tab_5)
        self.btnStopAcq_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btnStopAcq_2.setObjectName(_fromUtf8("btnStopAcq_2"))
        self.verticalLayout_16.addWidget(self.btnStopAcq_2)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem5)
        self.horizontalLayout_22.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtGui.QVBoxLayout()
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.lblChartHerePyQTGraph_2 = QtGui.QLabel(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblChartHerePyQTGraph_2.sizePolicy().hasHeightForWidth())
        self.lblChartHerePyQTGraph_2.setSizePolicy(sizePolicy)
        self.lblChartHerePyQTGraph_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblChartHerePyQTGraph_2.setObjectName(_fromUtf8("lblChartHerePyQTGraph_2"))
        self.verticalLayout_17.addWidget(self.lblChartHerePyQTGraph_2)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.btnAddRandomToChart_3 = QtGui.QPushButton(self.tab_5)
        self.btnAddRandomToChart_3.setObjectName(_fromUtf8("btnAddRandomToChart_3"))
        self.horizontalLayout_21.addWidget(self.btnAddRandomToChart_3)
        self.btnAddSinToChart_3 = QtGui.QPushButton(self.tab_5)
        self.btnAddSinToChart_3.setObjectName(_fromUtf8("btnAddSinToChart_3"))
        self.horizontalLayout_21.addWidget(self.btnAddSinToChart_3)
        self.btnClearChart_3 = QtGui.QPushButton(self.tab_5)
        self.btnClearChart_3.setObjectName(_fromUtf8("btnClearChart_3"))
        self.horizontalLayout_21.addWidget(self.btnClearChart_3)
        self.verticalLayout_17.addLayout(self.horizontalLayout_21)
        self.lblStatusChart_3 = QtGui.QLabel(self.tab_5)
        self.lblStatusChart_3.setObjectName(_fromUtf8("lblStatusChart_3"))
        self.verticalLayout_17.addWidget(self.lblStatusChart_3)
        self.horizontalLayout_22.addLayout(self.verticalLayout_17)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Arduino Plotter Library Example", None))
        self.label.setText(_translate("MainWindow", "Options:", None))
        self.btnEnqueue.setText(_translate("MainWindow", "Enqueue", None))
        self.btnDequeue.setText(_translate("MainWindow", "Dequeue", None))
        self.btnClear.setText(_translate("MainWindow", "Clear", None))
        self.lblStatus.setText(_translate("MainWindow", "Status:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "CircularBuffer", None))
        self.label_10.setText(_translate("MainWindow", "Options:", None))
        self.btnEnqueue_3.setText(_translate("MainWindow", "Enqueue", None))
        self.btnDequeue_3.setText(_translate("MainWindow", "Dequeue", None))
        self.btnClear_3.setText(_translate("MainWindow", "Clear", None))
        self.lblStatus_3.setText(_translate("MainWindow", "Status:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("MainWindow", "Queue", None))
        self.label_2.setText(_translate("MainWindow", "Options:", None))
        self.btnStartThr.setText(_translate("MainWindow", "Start", None))
        self.btnPauseThr.setText(_translate("MainWindow", "Pause", None))
        self.btnResumeThr.setText(_translate("MainWindow", "Resume", None))
        self.btnStopThr.setText(_translate("MainWindow", "Stop", None))
        self.label_3.setText(_translate("MainWindow", "Resultado:", None))
        self.lblResultThr.setText(_translate("MainWindow", "Status:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "QThreadHandler", None))
        self.label_11.setText(_translate("MainWindow", "Options:", None))
        self.btnStartThr_4.setText(_translate("MainWindow", "Start", None))
        self.btnPauseThr_4.setText(_translate("MainWindow", "Pause", None))
        self.btnResumeThr_4.setText(_translate("MainWindow", "Resume", None))
        self.btnStopThr_4.setText(_translate("MainWindow", "Stop", None))
        self.label_12.setText(_translate("MainWindow", "Resultado:", None))
        self.lblResultThr_3.setText(_translate("MainWindow", "Status:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), _translate("MainWindow", "ThreadHandler", None))
        self.label_8.setText(_translate("MainWindow", "Options:", None))
        self.btnStartAcq.setText(_translate("MainWindow", "Start Acquisition", None))
        self.btnPauseConsumer.setText(_translate("MainWindow", "Pause Consumer", None))
        self.btnResumeConsumer.setText(_translate("MainWindow", "Resume Consumer", None))
        self.btnStopAcq.setText(_translate("MainWindow", "Stop Acquisition", None))
        self.label_9.setText(_translate("MainWindow", "Resultado:", None))
        self.lblResultAcq.setText(_translate("MainWindow", "Status:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "ArduinoHandler", None))
        self.lblChartHereMatplotlib.setText(_translate("MainWindow", "Here will be a chart", None))
        self.btnAddRandomToChart.setText(_translate("MainWindow", "Add Random Point", None))
        self.btnAddSinToChart.setText(_translate("MainWindow", "Add Sin Point", None))
        self.btnClearChart.setText(_translate("MainWindow", "Clear", None))
        self.lblStatusChart.setText(_translate("MainWindow", "Status:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "MatPlotLibHandler", None))
        self.lblChartHerePyQTGraph.setText(_translate("MainWindow", "Here will be a chart", None))
        self.btnAddRandomToChart_2.setText(_translate("MainWindow", "Add Random Point", None))
        self.btnAddSinToChart_2.setText(_translate("MainWindow", "Add Sin Point", None))
        self.btnClearChart_2.setText(_translate("MainWindow", "Clear", None))
        self.lblStatusChart_2.setText(_translate("MainWindow", "Status:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), _translate("MainWindow", "PyQTGraphHandler", None))
        self.label_13.setText(_translate("MainWindow", "Options:", None))
        self.btnStartAcq_2.setText(_translate("MainWindow", "Start Acquisition", None))
        self.btnPauseConsumer_2.setText(_translate("MainWindow", "Pause Consumer", None))
        self.btnResumeConsumer_2.setText(_translate("MainWindow", "Resume Consumer", None))
        self.btnStopAcq_2.setText(_translate("MainWindow", "Stop Acquisition", None))
        self.lblChartHerePyQTGraph_2.setText(_translate("MainWindow", "Here will be a chart", None))
        self.btnAddRandomToChart_3.setText(_translate("MainWindow", "Add Random Point", None))
        self.btnAddSinToChart_3.setText(_translate("MainWindow", "Add Sin Point", None))
        self.btnClearChart_3.setText(_translate("MainWindow", "Clear", None))
        self.lblStatusChart_3.setText(_translate("MainWindow", "Status:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "ArduinoPlotter", None))
        self.menuArquivo.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))

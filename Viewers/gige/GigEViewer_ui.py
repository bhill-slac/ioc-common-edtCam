# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GigEViewer.ui'
#
# Created: Tue Jun 19 13:40:32 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 686)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.hboxlayout = QtGui.QHBoxLayout(self.centralwidget)
        self.hboxlayout.setObjectName("hboxlayout")
        self.widget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(234, 620))
        self.widget.setMaximumSize(QtCore.QSize(234, 16777215))
        self.widget.setObjectName("widget")
        self.vboxlayout = QtGui.QVBoxLayout(self.widget)
        self.vboxlayout.setObjectName("vboxlayout")
        self.frame_2 = QtGui.QFrame(self.widget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridlayout = QtGui.QGridLayout(self.frame_2)
        self.gridlayout.setObjectName("gridlayout")
        self.label_21 = QtGui.QLabel(self.frame_2)
        self.label_21.setMinimumSize(QtCore.QSize(80, 0))
        self.label_21.setObjectName("label_21")
        self.gridlayout.addWidget(self.label_21, 0, 0, 1, 1)
        self.lPV = QtGui.QLabel(self.frame_2)
        self.lPV.setText("")
        self.lPV.setObjectName("lPV")
        self.gridlayout.addWidget(self.lPV, 0, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.frame_2)
        self.label_16.setObjectName("label_16")
        self.gridlayout.addWidget(self.label_16, 1, 0, 1, 1)
        self.lImgCounter = QtGui.QLabel(self.frame_2)
        self.lImgCounter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lImgCounter.setObjectName("lImgCounter")
        self.gridlayout.addWidget(self.lImgCounter, 1, 1, 1, 1)
        self.label_17 = QtGui.QLabel(self.frame_2)
        self.label_17.setObjectName("label_17")
        self.gridlayout.addWidget(self.label_17, 2, 0, 1, 1)
        self.lImgRate = QtGui.QLabel(self.frame_2)
        self.lImgRate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lImgRate.setObjectName("lImgRate")
        self.gridlayout.addWidget(self.lImgRate, 2, 1, 1, 1)
        self.label_26 = QtGui.QLabel(self.frame_2)
        self.label_26.setObjectName("label_26")
        self.gridlayout.addWidget(self.label_26, 3, 0, 1, 1)
        self.label_rate = QtGui.QLabel(self.frame_2)
        self.label_rate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_rate.setObjectName("label_rate")
        self.gridlayout.addWidget(self.label_rate, 3, 1, 1, 1)
        self.vboxlayout.addWidget(self.frame_2)
        self.toolBox = QtGui.QToolBox(self.widget)
        self.toolBox.setFrameShape(QtGui.QFrame.StyledPanel)
        self.toolBox.setObjectName("toolBox")
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 96, 26))
        self.page.setObjectName("page")
        self.layoutWidget = QtGui.QWidget(self.page)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 211, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.layoutWidget)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setObjectName("gridlayout1")
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(65, 0))
        self.label.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label.setObjectName("label")
        self.gridlayout1.addWidget(self.label, 0, 0, 1, 1)
        self.leExpTime = QtGui.QLineEdit(self.layoutWidget)
        self.leExpTime.setMinimumSize(QtCore.QSize(75, 0))
        self.leExpTime.setMaximumSize(QtCore.QSize(75, 16777215))
        self.leExpTime.setObjectName("leExpTime")
        self.gridlayout1.addWidget(self.leExpTime, 0, 1, 1, 1)
        self.lExpTime = QtGui.QLabel(self.layoutWidget)
        self.lExpTime.setMinimumSize(QtCore.QSize(35, 0))
        self.lExpTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lExpTime.setObjectName("lExpTime")
        self.gridlayout1.addWidget(self.lExpTime, 0, 2, 1, 2)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(65, 0))
        self.label_3.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label_3.setObjectName("label_3")
        self.gridlayout1.addWidget(self.label_3, 1, 0, 1, 1)
        self.leExpPeriod = QtGui.QLineEdit(self.layoutWidget)
        self.leExpPeriod.setMinimumSize(QtCore.QSize(75, 0))
        self.leExpPeriod.setMaximumSize(QtCore.QSize(75, 16777215))
        self.leExpPeriod.setObjectName("leExpPeriod")
        self.gridlayout1.addWidget(self.leExpPeriod, 1, 1, 1, 2)
        self.lExpPeriod = QtGui.QLabel(self.layoutWidget)
        self.lExpPeriod.setMinimumSize(QtCore.QSize(35, 0))
        self.lExpPeriod.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lExpPeriod.setObjectName("lExpPeriod")
        self.gridlayout1.addWidget(self.lExpPeriod, 1, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(65, 0))
        self.label_5.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label_5.setObjectName("label_5")
        self.gridlayout1.addWidget(self.label_5, 2, 0, 1, 1)
        self.leGain = QtGui.QLineEdit(self.layoutWidget)
        self.leGain.setMinimumSize(QtCore.QSize(75, 0))
        self.leGain.setMaximumSize(QtCore.QSize(75, 16777215))
        self.leGain.setObjectName("leGain")
        self.gridlayout1.addWidget(self.leGain, 2, 1, 1, 1)
        self.lGain = QtGui.QLabel(self.layoutWidget)
        self.lGain.setMinimumSize(QtCore.QSize(35, 0))
        self.lGain.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lGain.setObjectName("lGain")
        self.gridlayout1.addWidget(self.lGain, 2, 2, 1, 2)
        self.vboxlayout1.addLayout(self.gridlayout1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout1.addItem(spacerItem)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 212, 207))
        self.page_2.setObjectName("page_2")
        self.layoutWidget1 = QtGui.QWidget(self.page_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 10, 211, 191))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.vboxlayout2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.gridlayout2 = QtGui.QGridLayout()
        self.gridlayout2.setObjectName("gridlayout2")
        self.label_29 = QtGui.QLabel(self.layoutWidget1)
        self.label_29.setMinimumSize(QtCore.QSize(0, 0))
        self.label_29.setObjectName("label_29")
        self.gridlayout2.addWidget(self.label_29, 0, 0, 1, 1)
        self.leRoiXStart = QtGui.QLineEdit(self.layoutWidget1)
        self.leRoiXStart.setMaximumSize(QtCore.QSize(75, 16777215))
        self.leRoiXStart.setObjectName("leRoiXStart")
        self.gridlayout2.addWidget(self.leRoiXStart, 0, 1, 1, 1)
        self.lRoiXStart = QtGui.QLabel(self.layoutWidget1)
        self.lRoiXStart.setMinimumSize(QtCore.QSize(35, 0))
        self.lRoiXStart.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lRoiXStart.setObjectName("lRoiXStart")
        self.gridlayout2.addWidget(self.lRoiXStart, 0, 2, 1, 1)
        self.label_30 = QtGui.QLabel(self.layoutWidget1)
        self.label_30.setMinimumSize(QtCore.QSize(0, 0))
        self.label_30.setObjectName("label_30")
        self.gridlayout2.addWidget(self.label_30, 1, 0, 1, 1)
        self.leRoiXSize = QtGui.QLineEdit(self.layoutWidget1)
        self.leRoiXSize.setMaximumSize(QtCore.QSize(75, 16777215))
        self.leRoiXSize.setObjectName("leRoiXSize")
        self.gridlayout2.addWidget(self.leRoiXSize, 1, 1, 1, 1)
        self.lRoiXSize = QtGui.QLabel(self.layoutWidget1)
        self.lRoiXSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lRoiXSize.setObjectName("lRoiXSize")
        self.gridlayout2.addWidget(self.lRoiXSize, 1, 2, 1, 1)
        self.label_27 = QtGui.QLabel(self.layoutWidget1)
        self.label_27.setMinimumSize(QtCore.QSize(65, 0))
        self.label_27.setObjectName("label_27")
        self.gridlayout2.addWidget(self.label_27, 2, 0, 1, 1)
        self.leRoiYStart = QtGui.QLineEdit(self.layoutWidget1)
        self.leRoiYStart.setMaximumSize(QtCore.QSize(75, 16777215))
        self.leRoiYStart.setObjectName("leRoiYStart")
        self.gridlayout2.addWidget(self.leRoiYStart, 2, 1, 1, 1)
        self.lRoiYStart = QtGui.QLabel(self.layoutWidget1)
        self.lRoiYStart.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lRoiYStart.setObjectName("lRoiYStart")
        self.gridlayout2.addWidget(self.lRoiYStart, 2, 2, 1, 1)
        self.label_18 = QtGui.QLabel(self.layoutWidget1)
        self.label_18.setMinimumSize(QtCore.QSize(65, 0))
        self.label_18.setObjectName("label_18")
        self.gridlayout2.addWidget(self.label_18, 3, 0, 1, 1)
        self.leRoiYSize = QtGui.QLineEdit(self.layoutWidget1)
        self.leRoiYSize.setMaximumSize(QtCore.QSize(75, 16777215))
        self.leRoiYSize.setObjectName("leRoiYSize")
        self.gridlayout2.addWidget(self.leRoiYSize, 3, 1, 1, 1)
        self.lRoiYSize = QtGui.QLabel(self.layoutWidget1)
        self.lRoiYSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lRoiYSize.setObjectName("lRoiYSize")
        self.gridlayout2.addWidget(self.lRoiYSize, 3, 2, 1, 1)
        self.vboxlayout2.addLayout(self.gridlayout2)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.bSelectROI = QtGui.QToolButton(self.layoutWidget1)
        icon = QtGui.QIcon()
        icon.addFile(":/new/prefix1/images/Crop3.png")
        self.bSelectROI.setIcon(icon)
        self.bSelectROI.setIconSize(QtCore.QSize(24, 24))
        self.bSelectROI.setCheckable(True)
        self.bSelectROI.setObjectName("bSelectROI")
        self.hboxlayout1.addWidget(self.bSelectROI)
        self.bClearROI = QtGui.QToolButton(self.layoutWidget1)
        icon1 = QtGui.QIcon()
        icon1.addFile(":/new/prefix1/images/FullImage3.png")
        self.bClearROI.setIcon(icon1)
        self.bClearROI.setIconSize(QtCore.QSize(24, 24))
        self.bClearROI.setObjectName("bClearROI")
        self.hboxlayout1.addWidget(self.bClearROI)
        self.vboxlayout2.addLayout(self.hboxlayout1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem1)
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 96, 26))
        self.page_3.setObjectName("page_3")
        self.layoutWidget2 = QtGui.QWidget(self.page_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 10, 211, 191))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.vboxlayout3 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.gridlayout3 = QtGui.QGridLayout()
        self.gridlayout3.setObjectName("gridlayout3")
        self.label_31 = QtGui.QLabel(self.layoutWidget2)
        self.label_31.setMinimumSize(QtCore.QSize(65, 0))
        self.label_31.setMaximumSize(QtCore.QSize(65, 16777215))
        self.label_31.setObjectName("label_31")
        self.gridlayout3.addWidget(self.label_31, 0, 0, 1, 1)
        self.leBinX = QtGui.QLineEdit(self.layoutWidget2)
        self.leBinX.setMinimumSize(QtCore.QSize(0, 27))
        self.leBinX.setMaximumSize(QtCore.QSize(75, 16777215))
        self.leBinX.setObjectName("leBinX")
        self.gridlayout3.addWidget(self.leBinX, 0, 1, 1, 1)
        self.lBinX = QtGui.QLabel(self.layoutWidget2)
        self.lBinX.setMinimumSize(QtCore.QSize(35, 0))
        self.lBinX.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lBinX.setObjectName("lBinX")
        self.gridlayout3.addWidget(self.lBinX, 0, 2, 1, 1)
        self.vboxlayout3.addLayout(self.gridlayout3)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout3.addItem(spacerItem2)
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtGui.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 96, 26))
        self.page_4.setObjectName("page_4")
        self.layoutWidget3 = QtGui.QWidget(self.page_4)
        self.layoutWidget3.setGeometry(QtCore.QRect(0, 0, 211, 211))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.vboxlayout4 = QtGui.QVBoxLayout(self.layoutWidget3)
        self.vboxlayout4.setObjectName("vboxlayout4")
        self.gridlayout4 = QtGui.QGridLayout()
        self.gridlayout4.setObjectName("gridlayout4")
        self.label_32 = QtGui.QLabel(self.layoutWidget3)
        self.label_32.setMinimumSize(QtCore.QSize(0, 28))
        self.label_32.setObjectName("label_32")
        self.gridlayout4.addWidget(self.label_32, 0, 0, 1, 1)
        self.cbImageMode = QtGui.QComboBox(self.layoutWidget3)
        self.cbImageMode.setMinimumSize(QtCore.QSize(0, 26))
        self.cbImageMode.setObjectName("cbImageMode")
        self.gridlayout4.addWidget(self.cbImageMode, 0, 1, 1, 1)
        self.label_33 = QtGui.QLabel(self.layoutWidget3)
        self.label_33.setMinimumSize(QtCore.QSize(0, 28))
        self.label_33.setObjectName("label_33")
        self.gridlayout4.addWidget(self.label_33, 1, 0, 1, 1)
        self.cbTriggerMode = QtGui.QComboBox(self.layoutWidget3)
        self.cbTriggerMode.setMinimumSize(QtCore.QSize(0, 26))
        self.cbTriggerMode.setObjectName("cbTriggerMode")
        self.gridlayout4.addWidget(self.cbTriggerMode, 1, 1, 1, 1)
        self.vboxlayout4.addLayout(self.gridlayout4)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout4.addItem(spacerItem3)
        self.toolBox.addItem(self.page_4, "")
        self.page_5 = QtGui.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 212, 207))
        self.page_5.setMinimumSize(QtCore.QSize(0, 0))
        self.page_5.setObjectName("page_5")
        self.layoutWidget4 = QtGui.QWidget(self.page_5)
        self.layoutWidget4.setGeometry(QtCore.QRect(6, 10, 204, 191))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.vboxlayout5 = QtGui.QVBoxLayout(self.layoutWidget4)
        self.vboxlayout5.setObjectName("vboxlayout5")
        self.gridlayout5 = QtGui.QGridLayout()
        self.gridlayout5.setObjectName("gridlayout5")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout5.addItem(spacerItem4, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget4)
        self.label_2.setObjectName("label_2")
        self.gridlayout5.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget4)
        self.label_6.setObjectName("label_6")
        self.gridlayout5.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget4)
        self.label_7.setObjectName("label_7")
        self.gridlayout5.addWidget(self.label_7, 1, 0, 1, 1)
        self.leCross1X = QtGui.QLineEdit(self.layoutWidget4)
        self.leCross1X.setMaximumSize(QtCore.QSize(65, 16777215))
        self.leCross1X.setObjectName("leCross1X")
        self.gridlayout5.addWidget(self.leCross1X, 1, 1, 1, 1)
        self.leCross2X = QtGui.QLineEdit(self.layoutWidget4)
        self.leCross2X.setMaximumSize(QtCore.QSize(65, 16777215))
        self.leCross2X.setObjectName("leCross2X")
        self.gridlayout5.addWidget(self.leCross2X, 1, 2, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget4)
        self.label_8.setObjectName("label_8")
        self.gridlayout5.addWidget(self.label_8, 2, 0, 1, 1)
        self.leCross1Y = QtGui.QLineEdit(self.layoutWidget4)
        self.leCross1Y.setMaximumSize(QtCore.QSize(65, 16777215))
        self.leCross1Y.setObjectName("leCross1Y")
        self.gridlayout5.addWidget(self.leCross1Y, 2, 1, 1, 1)
        self.leCross2Y = QtGui.QLineEdit(self.layoutWidget4)
        self.leCross2Y.setMaximumSize(QtCore.QSize(65, 16777215))
        self.leCross2Y.setObjectName("leCross2Y")
        self.gridlayout5.addWidget(self.leCross2Y, 2, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.layoutWidget4)
        self.label_11.setObjectName("label_11")
        self.gridlayout5.addWidget(self.label_11, 3, 0, 1, 1)
        self.cbCross1Color = QtGui.QComboBox(self.layoutWidget4)
        self.cbCross1Color.setMaximumSize(QtCore.QSize(65, 16777215))
        self.cbCross1Color.setObjectName("cbCross1Color")
        self.gridlayout5.addWidget(self.cbCross1Color, 3, 1, 1, 1)
        self.cbCross2Color = QtGui.QComboBox(self.layoutWidget4)
        self.cbCross2Color.setMaximumSize(QtCore.QSize(65, 16777215))
        self.cbCross2Color.setObjectName("cbCross2Color")
        self.gridlayout5.addWidget(self.cbCross2Color, 3, 2, 1, 1)
        self.bCross1 = QtGui.QToolButton(self.layoutWidget4)
        icon2 = QtGui.QIcon()
        icon2.addFile(":/new/prefix1/images/Click3.png")
        self.bCross1.setIcon(icon2)
        self.bCross1.setCheckable(True)
        self.bCross1.setObjectName("bCross1")
        self.gridlayout5.addWidget(self.bCross1, 4, 1, 1, 1)
        self.bCross2 = QtGui.QToolButton(self.layoutWidget4)
        self.bCross2.setIcon(icon2)
        self.bCross2.setCheckable(True)
        self.bCross2.setObjectName("bCross2")
        self.gridlayout5.addWidget(self.bCross2, 4, 2, 1, 1)
        self.vboxlayout5.addLayout(self.gridlayout5)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout5.addItem(spacerItem5)
        self.toolBox.addItem(self.page_5, "")
        self.page_6 = QtGui.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 96, 26))
        self.page_6.setObjectName("page_6")
        self.layoutWidget5 = QtGui.QWidget(self.page_6)
        self.layoutWidget5.setGeometry(QtCore.QRect(11, 1, 193, 246))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.vboxlayout6 = QtGui.QVBoxLayout(self.layoutWidget5)
        self.vboxlayout6.setObjectName("vboxlayout6")
        self.gridlayout6 = QtGui.QGridLayout()
        self.gridlayout6.setObjectName("gridlayout6")
        self.label_4 = QtGui.QLabel(self.layoutWidget5)
        self.label_4.setObjectName("label_4")
        self.gridlayout6.addWidget(self.label_4, 0, 0, 1, 1)
        self.lePath = QtGui.QLineEdit(self.layoutWidget5)
        self.lePath.setObjectName("lePath")
        self.gridlayout6.addWidget(self.lePath, 0, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.layoutWidget5)
        self.label_9.setObjectName("label_9")
        self.gridlayout6.addWidget(self.label_9, 1, 0, 1, 1)
        self.leFile = QtGui.QLineEdit(self.layoutWidget5)
        self.leFile.setObjectName("leFile")
        self.gridlayout6.addWidget(self.leFile, 1, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.layoutWidget5)
        self.label_10.setObjectName("label_10")
        self.gridlayout6.addWidget(self.label_10, 2, 0, 1, 1)
        self.leNumber = QtGui.QLineEdit(self.layoutWidget5)
        self.leNumber.setObjectName("leNumber")
        self.gridlayout6.addWidget(self.leNumber, 2, 1, 1, 1)
        self.label_12 = QtGui.QLabel(self.layoutWidget5)
        self.label_12.setObjectName("label_12")
        self.gridlayout6.addWidget(self.label_12, 3, 0, 1, 1)
        self.lePeriod = QtGui.QLineEdit(self.layoutWidget5)
        self.lePeriod.setObjectName("lePeriod")
        self.gridlayout6.addWidget(self.lePeriod, 3, 1, 1, 1)
        self.vboxlayout6.addLayout(self.gridlayout6)
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem6)
        self.bSave = QtGui.QPushButton(self.layoutWidget5)
        self.bSave.setObjectName("bSave")
        self.hboxlayout2.addWidget(self.bSave)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem7)
        self.vboxlayout6.addLayout(self.hboxlayout2)
        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem8)
        self.bStopSave = QtGui.QPushButton(self.layoutWidget5)
        self.bStopSave.setObjectName("bStopSave")
        self.hboxlayout3.addWidget(self.bStopSave)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem9)
        self.vboxlayout6.addLayout(self.hboxlayout3)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout6.addItem(spacerItem10)
        self.toolBox.addItem(self.page_6, "")
        self.vboxlayout.addWidget(self.toolBox)
        self.frame_3 = QtGui.QFrame(self.widget)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridlayout7 = QtGui.QGridLayout(self.frame_3)
        self.gridlayout7.setObjectName("gridlayout7")
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout7.addItem(spacerItem11, 0, 0, 1, 1)
        self.bStart = QtGui.QPushButton(self.frame_3)
        self.bStart.setMaximumSize(QtCore.QSize(75, 16777215))
        self.bStart.setObjectName("bStart")
        self.gridlayout7.addWidget(self.bStart, 0, 1, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout7.addItem(spacerItem12, 0, 2, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout7.addItem(spacerItem13, 1, 0, 1, 1)
        self.bStop = QtGui.QPushButton(self.frame_3)
        self.bStop.setMaximumSize(QtCore.QSize(75, 16777215))
        self.bStop.setObjectName("bStop")
        self.gridlayout7.addWidget(self.bStop, 1, 1, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout7.addItem(spacerItem14, 1, 2, 1, 1)
        self.vboxlayout.addWidget(self.frame_3)
        self.hboxlayout.addWidget(self.widget)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(250, 250))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.hboxlayout4 = QtGui.QHBoxLayout(self.frame)
        self.hboxlayout4.setObjectName("hboxlayout4")
        self.wImage = QtGui.QWidget(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wImage.sizePolicy().hasHeightForWidth())
        self.wImage.setSizePolicy(sizePolicy)
        self.wImage.setObjectName("wImage")
        self.hboxlayout4.addWidget(self.wImage)
        self.hboxlayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Counter", None, QtGui.QApplication.UnicodeUTF8))
        self.lImgCounter.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "Frame Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.lImgRate.setText(QtGui.QApplication.translate("MainWindow", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("MainWindow", "Display Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rate.setText(QtGui.QApplication.translate("MainWindow", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Exp Time", None, QtGui.QApplication.UnicodeUTF8))
        self.lExpTime.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Period", None, QtGui.QApplication.UnicodeUTF8))
        self.lExpPeriod.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Gain", None, QtGui.QApplication.UnicodeUTF8))
        self.lGain.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("MainWindow", "Exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("MainWindow", "X Start", None, QtGui.QApplication.UnicodeUTF8))
        self.lRoiXStart.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("MainWindow", "X Size", None, QtGui.QApplication.UnicodeUTF8))
        self.lRoiXSize.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("MainWindow", "Y Start", None, QtGui.QApplication.UnicodeUTF8))
        self.lRoiYStart.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "Y Size", None, QtGui.QApplication.UnicodeUTF8))
        self.lRoiYSize.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.bSelectROI.setToolTip(QtGui.QApplication.translate("MainWindow", "Click and drag the mouse over the image to define the ROI", None, QtGui.QApplication.UnicodeUTF8))
        self.bSelectROI.setText(QtGui.QApplication.translate("MainWindow", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.bClearROI.setToolTip(QtGui.QApplication.translate("MainWindow", "Clear the ROI", None, QtGui.QApplication.UnicodeUTF8))
        self.bClearROI.setText(QtGui.QApplication.translate("MainWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("MainWindow", "ROI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("MainWindow", "X, Y", None, QtGui.QApplication.UnicodeUTF8))
        self.lBinX.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QtGui.QApplication.translate("MainWindow", "Binning", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("MainWindow", "Image Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_33.setText(QtGui.QApplication.translate("MainWindow", "Trigger Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QtGui.QApplication.translate("MainWindow", "Modes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Cross 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Cross 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Y", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.bCross1.setToolTip(QtGui.QApplication.translate("MainWindow", "Set Cross 1 by clicking the mouse on the image", None, QtGui.QApplication.UnicodeUTF8))
        self.bCross1.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.bCross2.setToolTip(QtGui.QApplication.translate("MainWindow", "Set Cross 1 by clicking the mouse on the image", None, QtGui.QApplication.UnicodeUTF8))
        self.bCross2.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QtGui.QApplication.translate("MainWindow", "Crosses", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.lePath.setText(QtGui.QApplication.translate("MainWindow", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.leFile.setText(QtGui.QApplication.translate("MainWindow", "img", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Count", None, QtGui.QApplication.UnicodeUTF8))
        self.leNumber.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Period", None, QtGui.QApplication.UnicodeUTF8))
        self.lePeriod.setText(QtGui.QApplication.translate("MainWindow", "1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.bSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.bStopSave.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), QtGui.QApplication.translate("MainWindow", "Saving", None, QtGui.QApplication.UnicodeUTF8))
        self.bStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.bStop.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.wImage.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background: dark gray", None, QtGui.QApplication.UnicodeUTF8))

import GigEViewer_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


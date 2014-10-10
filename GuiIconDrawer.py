# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'host.ui'
#
# Created: Wed Aug  6 12:26:57 2014
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import time
import PyTango
import taurus
from draw import DrawSVG 
import sys
#sys.path.append('pyglet')
import pyglet
from math import sqrt


from savetoxml import ToXML
import xml.etree.ElementTree as ETree
from PyQt4.QtGui import *
import operator
from PyQt4 import QtCore, QtGui
import addlayer
import copy

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


class Scroll(QGraphicsView):
    wheelEventSignal = QtCore.pyqtSignal(int, name = 'wheelEventSignal')
    mousePressSignal = QtCore.pyqtSignal(int, int, name = 'mousePressSignal')
    def __init__(self, ob, parent): 
        super(Scroll, self) .__init__(parent)
        path = str(ob.lineEdit_PictureName.text())+".svg"
        if os.path.isfile(path):
            ob.scene.addPixmap(QtGui.QPixmap(path))
        else:
            path = 'resources/' + path
            ob.scene.addPixmap(QtGui.QPixmap(path))
        ob.setScene(ob.scene)
        
    def mousePressEvent(self, event):
        super(Scroll, self).mousePressEvent(event)
        position_x = event.pos().x()
        position_y = event.pos().y()
        self.mousePressSignal.emit(position_x, position_y)
       
        
    def wheelEvent(self, event):
        super(Scroll, self).wheelEvent(event)
        print("wheelEvent", event.delta())
        tmp_int = event.delta()
        self.wheelEventSignal.emit(tmp_int)
        #print pictureFileName
        


class Ui_Widget(QGraphicsView):
    assignIconToDeviceSignal = QtCore.pyqtSignal(str, str, str, str, name = 'assignIconToDeviceSignal')
   
    def __init__(self, parent=None):
        super(Ui_Widget, self).__init__(parent)
    
   
    
        
    def setupUi(self, Dialog):
        self.xml=ToXML()
        self.svgwidth=250
        self.svgheight=250
        self.svg = DrawSVG("self.worksname", self.svgwidth, self.svgheight) 
        
        
        
        
        
        self.grview = QGraphicsView()
        self.scene = QGraphicsScene(self.grview) 
        
        self.listDeviceName=[] #lista do kotrej zapisuje nazwy urzadzen importowanych z xmla
        self.listPictureFileName=[] #lista do ktorej zapisuje nazwy obrazkow importowanych z xmla
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1200, 550)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1200, 480))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame.hide()
        
       
        
        self.frame_3 = QtGui.QFrame(self.frame)#frame to picture's color choosing (RGB or not)
        self.frame_3.setGeometry(QtCore.QRect(640, 150, 225, 100))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        
        self.frame_4 = QtGui.QFrame(self.frame)#frame to picture's color choosing (RGB or not)
        self.frame_4.setGeometry(QtCore.QRect(640, 270, 225, 200))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.frame_4.hide()
        
        self.frame_2 = QtGui.QFrame(Dialog)#frame to picture's file details
        self.frame_2.setGeometry(QtCore.QRect(0, 230, 230, 250))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.frame_2.hide()
        
        self.pushButton_Refresh = QtGui.QPushButton(self.frame) #Refresh
        self.pushButton_Refresh.setGeometry(QtCore.QRect(430, 420, 70, 27))
        self.pushButton_Refresh.setObjectName(_fromUtf8("pushButton_Refresh"))
        
        self.radioButton_DrawRGB = QtGui.QRadioButton(self.frame)
        self.radioButton_DrawRGB.setGeometry(QtCore.QRect(680, 250, 190, 22))
        self.radioButton_DrawRGB.setObjectName(_fromUtf8("radioButton_DrawRGB"))
        
        self.pushButton_AssignIconToDevice = QtGui.QPushButton(self.frame) #assign the icon to the device
        self.pushButton_AssignIconToDevice.setGeometry(QtCore.QRect(870, 380, 300, 27))
        self.pushButton_AssignIconToDevice.setObjectName(_fromUtf8("pushButton_AssignIconToDevice"))
        
        self.pushButton_AssignNameAndSizesToPicture = QtGui.QPushButton(self.frame_2) #assign picturefile name and picture sizes
        self.pushButton_AssignNameAndSizesToPicture.setGeometry(QtCore.QRect(30, 205, 190, 27))
        self.pushButton_AssignNameAndSizesToPicture.setObjectName(_fromUtf8("pushButton_AssignNameAndSizesToPicture"))
        
        self.pushButton_AddPictureToNewDevice = QtGui.QPushButton(Dialog) #add picture to new device
        self.pushButton_AddPictureToNewDevice.setGeometry(QtCore.QRect(20, 150, 190, 27))
        self.pushButton_AddPictureToNewDevice.setObjectName(_fromUtf8("pushButton_AddPictureToNewDevice"))
        
        self.pushButton_Draw = QtGui.QPushButton(self.frame) #drawing the picture
        self.pushButton_Draw.setGeometry(QtCore.QRect(350, 420, 70, 27))
        self.pushButton_Draw.setObjectName(_fromUtf8("pushButton_Draw"))
        
        self.pushButton_ImportFromXML = QtGui.QPushButton(Dialog) #import from xml
        self.pushButton_ImportFromXML.setGeometry(QtCore.QRect(20, 80, 190, 27))
        self.pushButton_ImportFromXML.setObjectName(_fromUtf8("pushButton_ImportFromXML"))
        
        self.pushButton_8 = QtGui.QPushButton(self.frame_2) #show assigned picture
        self.pushButton_8.setGeometry(QtCore.QRect(30, 205, 190, 27))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_8.hide()
        
        
        self.label_PictureName = QtGui.QLabel(self.frame_2)
        self.label_PictureName.setGeometry(QtCore.QRect(25, 30, 200, 17))
        self.label_PictureName.setText(_fromUtf8("Let's write picturefile's name:"))
        self.label_PictureName.setObjectName(_fromUtf8("label_PictureName"))
        """ start lineEdit_PictureNameor"""
        self.lineEdit_PictureName = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_PictureName.setGeometry(QtCore.QRect(50, 55, 104, 31))
        self.lineEdit_PictureName.setObjectName(_fromUtf8("lineEdit_PictureName"))
        
        self.label_PictureSizes = QtGui.QLabel(self.frame_2) # dimensions of picture
        self.label_PictureSizes.setGeometry(QtCore.QRect(25, 90, 250, 17))
        self.label_PictureSizes.setText(_fromUtf8("Let's write pictur's sizes in px:"))
        self.label_PictureSizes.setObjectName(_fromUtf8("label_PictureSizes"))
        
        self.label_PictureWidth = QtGui.QLabel(self.frame_2) #dimensions of picture width
        self.label_PictureWidth.setGeometry(QtCore.QRect(25, 120, 50, 17))
        self.label_PictureWidth.setText(_fromUtf8("width:"))
        self.label_PictureWidth.setObjectName(_fromUtf8("label_PictureWidth"))
        
        self.label_PictureHeight = QtGui.QLabel(self.frame_2) #dimensions of picture height
        self.label_PictureHeight.setGeometry(QtCore.QRect(25, 155, 50, 17))
        self.label_PictureHeight.setText(_fromUtf8("height:"))
        self.label_PictureHeight.setObjectName(_fromUtf8("label_PictureHeight"))
        """ start lineEdit_PictureNameor"""
        self.lineEdit_PictureWidth = QtGui.QLineEdit(self.frame_2) #giving dimensions of picture:width
        self.lineEdit_PictureWidth.setGeometry(QtCore.QRect(80, 115, 55, 31))
        self.lineEdit_PictureWidth.setObjectName(_fromUtf8("lineEdit_PictureWidth"))
        self.lineEdit_PictureWidth.setText("800")
        
        
        self.lineEdit_PictureHeight = QtGui.QLineEdit(self.frame_2) #giving dimensions of picture:height
        self.lineEdit_PictureHeight.setGeometry(QtCore.QRect(80, 155, 55, 31))
        self.lineEdit_PictureHeight.setObjectName(_fromUtf8("lineEdit_PictureHeight"))
        self.lineEdit_PictureHeight.setText("600")
        
        """ end lineEdit_PictureNameor""" 
        
        """start message button"""
        self.messageBox=QtGui.QMessageBox(Dialog)
        self.messageBox.setGeometry(QtCore.QRect(350, 350, 190, 22))
        self.messageBox.setObjectName(_fromUtf8("messageBox"))
        self.messageBox.setText("Let's write picturefile's name");
        """end message button"""
        
        
        self.comboBox_UnassignedDevices = QtGui.QComboBox(Dialog)
        self.comboBox_UnassignedDevices.setGeometry(QtCore.QRect(20, 190, 145, 27))
        self.comboBox_UnassignedDevices.setObjectName(_fromUtf8("comboBox_UnassignedDevices"))
        self.comboBox_UnassignedDevices.hide()
        
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 141, 17))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 121, 17))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        
        self.checkBox_Rectangle = QtGui.QCheckBox(self.frame)
        self.checkBox_Rectangle.setGeometry(QtCore.QRect(230, 40, 97, 22))
        self.checkBox_Rectangle.setObjectName(_fromUtf8("checkBox_Rectangle"))
        self.checkBox_Circle = QtGui.QCheckBox(self.frame)
        self.checkBox_Circle.setGeometry(QtCore.QRect(230, 100, 97, 22))
        self.checkBox_Circle.setObjectName(_fromUtf8("checkBox_Circle"))
        self.checkBox_Ellipse = QtGui.QCheckBox(self.frame)
        self.checkBox_Ellipse.setGeometry(QtCore.QRect(230, 160, 97, 22))
        self.checkBox_Ellipse.setObjectName(_fromUtf8("checkBox_Ellipse"))
        self.checkBox_Line = QtGui.QCheckBox(self.frame)
        self.checkBox_Line.setGeometry(QtCore.QRect(230, 220, 97, 22))
        self.checkBox_Line.setObjectName(_fromUtf8("checkBox_Line"))
        
        self.par_1 = QtGui.QCheckBox(self.frame)
        self.par_1.setGeometry(QtCore.QRect(350, 5, 97, 22))
        self.par_1.setObjectName(_fromUtf8("par_1"))
        self.par_2 = QtGui.QCheckBox(self.frame)
        self.par_2.setGeometry(QtCore.QRect(430, 5, 97, 22))
        self.par_2.setObjectName(_fromUtf8("par_2"))
        self.par_3 = QtGui.QCheckBox(self.frame)
        self.par_3.setGeometry(QtCore.QRect(510, 5, 97, 22))
        self.par_3.setObjectName(_fromUtf8("par_3"))
        self.par_4 = QtGui.QCheckBox(self.frame)
        self.par_4.setGeometry(QtCore.QRect(590, 5, 97, 22))
        self.par_4.setObjectName(_fromUtf8("par_4"))
        self.radioButton_add = QtGui.QRadioButton(self.frame)
        self.radioButton_add.setGeometry(QtCore.QRect(680, 10, 350, 22))
        self.radioButton_add.setObjectName(_fromUtf8("radioButton_add"))
        self.par_1.hide()
        self.par_2.hide()
        self.par_3.hide()
        self.par_4.hide()
    
            
        self.label_RectangleLeftUpX = QtGui.QLabel(self.frame)
        self.label_RectangleLeftUpX.setGeometry(QtCore.QRect(330, 20, 75, 20))
        self.label_RectangleLeftUpX.setText(_fromUtf8("left-up x"))
        
        self.spinBox_RectangleLeftUpX = QtGui.QSpinBox(self.frame)
        self.spinBox_RectangleLeftUpX.setGeometry(QtCore.QRect(330, 40, 55, 27))
        self.spinBox_RectangleLeftUpX.setObjectName(_fromUtf8("spinBox_RectangleLeftUpX"))
        self.spinBox_RectangleLeftUpX.setMaximum(1000)
        
        
        
        self.label_RectangleLeftUpY = QtGui.QLabel(self.frame)
        self.label_RectangleLeftUpY.setGeometry(QtCore.QRect(415, 20, 75, 20))
        self.label_RectangleLeftUpY.setText(_fromUtf8("left-up y"))
        self.spinBox_RectangleLeftUpY = QtGui.QSpinBox(self.frame)
        self.spinBox_RectangleLeftUpY.setGeometry(QtCore.QRect(415, 40, 55, 27))
        self.spinBox_RectangleLeftUpY.setObjectName(_fromUtf8("spinBox_RectangleLeftUpY"))
        self.spinBox_RectangleLeftUpY.setMaximum(1000)
        
        self.label_RectangleWidth = QtGui.QLabel(self.frame)
        self.label_RectangleWidth.setGeometry(QtCore.QRect(505, 20, 75, 20))
        self.label_RectangleWidth.setText(_fromUtf8("width"))
        self.spinBox_RectangleWidth = QtGui.QSpinBox(self.frame)
        self.spinBox_RectangleWidth.setGeometry(QtCore.QRect(500, 40, 55, 27))
        self.spinBox_RectangleWidth.setObjectName(_fromUtf8("spinBox_RectangleWidth"))
        self.spinBox_RectangleWidth.setMaximum(1000)
        
        

        
        self.label_RectangleHeight = QtGui.QLabel(self.frame)
        self.label_RectangleHeight.setGeometry(QtCore.QRect(590, 20, 75, 20))
        self.label_RectangleHeight.setText(_fromUtf8("height"))
        self.spinBox_RectangleHeight = QtGui.QSpinBox(self.frame)
        self.spinBox_RectangleHeight.setGeometry(QtCore.QRect(585, 40, 55, 27))
        self.spinBox_RectangleHeight.setObjectName(_fromUtf8("spinBox_RectangleHeight"))
        self.spinBox_RectangleHeight.setMaximum(1000)
        
        
      
        
        self.label_CircleCenterX = QtGui.QLabel(self.frame)
        self.label_CircleCenterX.setGeometry(QtCore.QRect(330, 80, 75, 20))
        self.label_CircleCenterX.setText(_fromUtf8("center x"))
        self.spinBox_CircleCenterX = QtGui.QSpinBox(self.frame)
        self.spinBox_CircleCenterX.setGeometry(QtCore.QRect(330, 100, 55, 27))
        self.spinBox_CircleCenterX.setObjectName(_fromUtf8("spinBox_CircleCenterX"))
        self.spinBox_CircleCenterX.setMaximum(1000)
        
        self.label_CircleCenterY = QtGui.QLabel(self.frame)
        self.label_CircleCenterY.setGeometry(QtCore.QRect(415, 80, 75, 20))
        self.label_CircleCenterY.setText(_fromUtf8("center y"))
        self.spinBox_CircleCenterY = QtGui.QSpinBox(self.frame)
        self.spinBox_CircleCenterY.setGeometry(QtCore.QRect(415, 100, 55, 27))
        self.spinBox_CircleCenterY.setObjectName(_fromUtf8("spinBox_CircleCenterY"))
        self.spinBox_CircleCenterY.setMaximum(1000)
        
        self.label_CircleRadius = QtGui.QLabel(self.frame)
        self.label_CircleRadius.setGeometry(QtCore.QRect(505, 80, 75, 20))
        self.label_CircleRadius.setText(_fromUtf8("radius"))
        self.spinBox_CircleRadius = QtGui.QSpinBox(self.frame)
        self.spinBox_CircleRadius.setGeometry(QtCore.QRect(500, 100, 55, 27))
        self.spinBox_CircleRadius.setObjectName(_fromUtf8("spinBox_CircleRadius"))
        self.spinBox_CircleRadius.setMaximum(1000)
        
        
        self.label_EllipseCenterX = QtGui.QLabel(self.frame)
        self.label_EllipseCenterX.setGeometry(QtCore.QRect(330, 140, 75, 20))
        self.label_EllipseCenterX.setText(_fromUtf8("center x"))
        self.spinBox_EllipseCenterX = QtGui.QSpinBox(self.frame)
        self.spinBox_EllipseCenterX.setGeometry(QtCore.QRect(330, 160, 55, 27))
        self.spinBox_EllipseCenterX.setObjectName(_fromUtf8("spinBox_EllipseCenterX"))
        self.spinBox_EllipseCenterX.setMaximum(1000)
        
        self.label_EllipseCenterY = QtGui.QLabel(self.frame)
        self.label_EllipseCenterY.setGeometry(QtCore.QRect(415, 140, 75, 20))
        self.label_EllipseCenterY.setText(_fromUtf8("center y"))
        self.spinBox_EllipseCenterY = QtGui.QSpinBox(self.frame)
        self.spinBox_EllipseCenterY.setGeometry(QtCore.QRect(415, 160, 55, 27))
        self.spinBox_EllipseCenterY.setObjectName(_fromUtf8("spinBox_EllipseCenterY"))
        self.spinBox_EllipseCenterY.setMaximum(1000)
        
        self.label_EllipseRadiiX = QtGui.QLabel(self.frame)
        self.label_EllipseRadiiX.setGeometry(QtCore.QRect(505, 140, 75, 20))
        self.label_EllipseRadiiX.setText(_fromUtf8("radii x"))
        self.spinBox_EllipseRadiiX = QtGui.QSpinBox(self.frame)
        self.spinBox_EllipseRadiiX.setGeometry(QtCore.QRect(500, 160, 55, 27))
        self.spinBox_EllipseRadiiX.setObjectName(_fromUtf8("spinBox_EllipseRadiiX"))
        self.spinBox_EllipseRadiiX.setMaximum(1000)
        
        self.label_EllipseRadiiY = QtGui.QLabel(self.frame)
        self.label_EllipseRadiiY.setGeometry(QtCore.QRect(590, 140, 75, 20))
        self.label_EllipseRadiiY.setText(_fromUtf8("radii y"))
        self.spinBox_EllipseRadiiY = QtGui.QSpinBox(self.frame)
        self.spinBox_EllipseRadiiY.setGeometry(QtCore.QRect(585, 160, 55, 27))
        self.spinBox_EllipseRadiiY.setObjectName(_fromUtf8("spinBox_EllipseRadiiY"))
        self.spinBox_EllipseRadiiY.setMaximum(1000)
        
        
        self.label_LineStartX = QtGui.QLabel(self.frame)
        self.label_LineStartX.setGeometry(QtCore.QRect(330, 200, 75, 20))
        self.label_LineStartX.setText(_fromUtf8("start x"))
        self.spinBox_LineStartX = QtGui.QSpinBox(self.frame)
        self.spinBox_LineStartX.setGeometry(QtCore.QRect(330, 220, 55, 27))
        self.spinBox_LineStartX.setObjectName(_fromUtf8("spinBox_LineStartX"))
        self.spinBox_LineStartX.setMaximum(1000)
        
        
        self.label_LineStartY = QtGui.QLabel(self.frame)
        self.label_LineStartY.setGeometry(QtCore.QRect(415, 200, 75, 20))
        self.label_LineStartY.setText(_fromUtf8("start y"))
        self.spinBox_LineStartY = QtGui.QSpinBox(self.frame)
        self.spinBox_LineStartY.setGeometry(QtCore.QRect(415, 220, 55, 27))
        self.spinBox_LineStartY.setObjectName(_fromUtf8("spinBox_LineStartY"))
        self.spinBox_LineStartY.setMaximum(1000)
        
        
        self.label_LineEndX = QtGui.QLabel(self.frame)
        self.label_LineEndX.setGeometry(QtCore.QRect(505, 200, 75, 20))
        self.label_LineEndX.setText(_fromUtf8("end x"))
        self.spinBox_LineEndX = QtGui.QSpinBox(self.frame)
        self.spinBox_LineEndX.setGeometry(QtCore.QRect(500, 220, 55, 27))
        self.spinBox_LineEndX.setObjectName(_fromUtf8("spinBox_LineEndX"))
        self.spinBox_LineEndX.setMaximum(1000)
        
        
        self.label_LineEndY = QtGui.QLabel(self.frame)
        self.label_LineEndY.setGeometry(QtCore.QRect(590, 200, 75, 20))
        self.label_LineEndY.setText(_fromUtf8("end y"))
        self.spinBox_LineEndY = QtGui.QSpinBox(self.frame)
        self.spinBox_LineEndY.setGeometry(QtCore.QRect(585, 220, 55, 27))
        self.spinBox_LineEndY.setObjectName(_fromUtf8("spinBox_LineEndY"))
        self.spinBox_LineEndY.setMaximum(1000)
        
        
        colorList=["white","red", "green", "yellow", "blue", "black"]
        
        self.label_PictureFillColor = QtGui.QLabel(self.frame_3)
        self.label_PictureFillColor.setGeometry(QtCore.QRect(20, 10, 75, 20))
        self.label_PictureFillColor.setText(_fromUtf8("fill color"))
        self.comboBox_UnassignedDevices_PicturFillColors = QtGui.QComboBox(self.frame_3)
        self.comboBox_UnassignedDevices_PicturFillColors.setGeometry(QtCore.QRect(20, 30, 55, 27))
        self.comboBox_UnassignedDevices_PicturFillColors.setObjectName(_fromUtf8("comboBox_UnassignedDevices_PicturFillColors"))
        self.comboBox_UnassignedDevices_PicturFillColors.addItems(colorList)
        
        
        self.comboBox_AssignedDevices = QtGui.QComboBox(Dialog) #show imported data from xml
        self.comboBox_AssignedDevices.setGeometry(QtCore.QRect(20, 100, 150, 27))
        self.comboBox_AssignedDevices.setObjectName(_fromUtf8("comboBox_AssignedDevices"))
        self.comboBox_AssignedDevices.hide()
        
        
        self.label_PictureBorderColor = QtGui.QLabel(self.frame_3)
        self.label_PictureBorderColor.setGeometry(QtCore.QRect(110, 10, 85, 20))
        self.label_PictureBorderColor.setText(_fromUtf8("border color"))
        self.comboBox_PictureBorderColor = QtGui.QComboBox(self.frame_3)
        self.comboBox_PictureBorderColor.setGeometry(QtCore.QRect(110, 30, 55, 27))
        self.comboBox_PictureBorderColor.setObjectName(_fromUtf8("comboBox_PictureBorderColor"))
        self.comboBox_PictureBorderColor.addItems(colorList)
        
        
        self.label_PictureFillColorRGB = QtGui.QLabel(self.frame_4)
        self.label_PictureFillColorRGB.setGeometry(QtCore.QRect(50, 10, 75, 20))
        self.label_PictureFillColorRGB.setText(_fromUtf8("fill color"))
      
        self.label_PictureBorderColorRGB = QtGui.QLabel(self.frame_4)
        self.label_PictureBorderColorRGB.setGeometry(QtCore.QRect(134, 10, 85, 20))
        self.label_PictureBorderColorRGB.setText(_fromUtf8("border color"))
        
        
        self.label_PictureFillColorRed = QtGui.QLabel(self.frame_4)
        self.label_PictureFillColorRed.setGeometry(QtCore.QRect(5, 37, 75, 20))
        self.label_PictureFillColorRed.setText(_fromUtf8("red"))
        self.spinBox_PictureFillColorRed = QtGui.QSpinBox(self.frame_4)
        self.spinBox_PictureFillColorRed.setGeometry(QtCore.QRect(50, 35, 55, 27))
        self.spinBox_PictureFillColorRed.setObjectName(_fromUtf8("spinBox_PictureFillColorRed"))
        self.spinBox_PictureFillColorRed.setMaximum(255)
        self.spinBox_PictureBorderColorRed = QtGui.QSpinBox(self.frame_4)
        self.spinBox_PictureBorderColorRed.setGeometry(QtCore.QRect(150, 35, 55, 27))
        self.spinBox_PictureBorderColorRed.setObjectName(_fromUtf8("spinBox_PictureBorderColorRed"))
        self.spinBox_PictureBorderColorRed.setMaximum(255)
        
        self.label_PictureFillColorGreen = QtGui.QLabel(self.frame_4)
        self.label_PictureFillColorGreen.setGeometry(QtCore.QRect(5, 87, 75, 20))
        self.label_PictureFillColorGreen.setText(_fromUtf8("green"))
        self.spinBox_PictureFillColorGreen = QtGui.QSpinBox(self.frame_4)
        self.spinBox_PictureFillColorGreen.setGeometry(QtCore.QRect(50, 85, 55, 27))
        self.spinBox_PictureFillColorGreen.setObjectName(_fromUtf8("spinBox_PictureFillColorGreen"))
        self.spinBox_PictureFillColorGreen.setMaximum(255)
        self.spinBox_PictureBorderColorGreen = QtGui.QSpinBox(self.frame_4)
        self.spinBox_PictureBorderColorGreen.setGeometry(QtCore.QRect(150, 85, 55, 27))
        self.spinBox_PictureBorderColorGreen.setObjectName(_fromUtf8("spinBox_PictureBorderColorGreen"))
        self.spinBox_PictureBorderColorGreen.setMaximum(255)
        
        self.label_PictureFillColorBlue = QtGui.QLabel(self.frame_4)
        self.label_PictureFillColorBlue.setGeometry(QtCore.QRect(5, 137, 75, 20))
        self.label_PictureFillColorBlue.setText(_fromUtf8("blue"))
        self.spinBox_PictureFillColorBlue = QtGui.QSpinBox(self.frame_4)
        self.spinBox_PictureFillColorBlue.setGeometry(QtCore.QRect(50, 135, 55, 27))
        self.spinBox_PictureFillColorBlue.setObjectName(_fromUtf8("spinBox_PictureFillColorBlue"))
        self.spinBox_PictureFillColorBlue.setMaximum(255)
        self.spinBox_PictureBorderColorBlue = QtGui.QSpinBox(self.frame_4)
        self.spinBox_PictureBorderColorBlue.setGeometry(QtCore.QRect(150, 135, 55, 27))
        self.spinBox_PictureBorderColorBlue.setObjectName(_fromUtf8("spinBox_PictureBorderColorBlue"))
        self.spinBox_PictureBorderColorBlue.setMaximum(255)
        
        
        
        
        
        self.graphicsView = Scroll(self, self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(870, 40, 300, 300))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.wheel_integer_count=0

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
        #QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.click)

        QtCore.QObject.connect(self.pushButton_Refresh, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clicked_Refresh_button) #Refresh_button
        QtCore.QObject.connect(self.pushButton_AssignIconToDevice, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clicked_AssignIconToDevice_button)
        QtCore.QObject.connect(self.pushButton_AssignNameAndSizesToPicture, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clicked_AssignNameAndSizesToPicture_button)
        QtCore.QObject.connect(self.pushButton_ImportFromXML, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clicked_ImportFromXML_button) #Draw_button
        QtCore.QObject.connect(self.pushButton_Draw, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clicked_Draw_button)
        QtCore.QObject.connect(self.pushButton_AddPictureToNewDevice, QtCore.SIGNAL(_fromUtf8("clicked()")), self.clicked_AddPictureToNewDevice_button)
        
        QtCore.QObject.connect(self.radioButton_DrawRGB, QtCore.SIGNAL(_fromUtf8("pressed()")), self.clickedradioButton_DrawRGB)
        QtCore.QObject.connect(self.radioButton_add, QtCore.SIGNAL(_fromUtf8("pressed()")), self.clickedradioButton_add)
        
        QtCore.QObject.connect(self.comboBox_UnassignedDevices, QtCore.SIGNAL(_fromUtf8("activated (const QString&)")), self.choosen_UnassignedDevices_comboBox)
        QtCore.QObject.connect(self.comboBox_AssignedDevices, QtCore.SIGNAL(_fromUtf8("activated (const QString&)")), self.choosen_AssignedDevices_comboBox)
        self.graphicsView.wheelEventSignal.connect(self.wheelEventEncountered)
        self.graphicsView.mousePressSignal.connect(self.mousePress)
        
    def mousePress(self, parx, pary):
        print (parx, "     ", pary)
        if self.par_1.isChecked():
            if self.checkBox_Rectangle.isChecked():
                self.spinBox_RectangleLeftUpX.clear()
                self.spinBox_RectangleLeftUpX.setValue(parx)
            if self.checkBox_Circle.isChecked():
                self.spinBox_CircleCenterX.clear()
                self.spinBox_CircleCenterX.setValue(parx)
            if self.checkBox_Ellipse.isChecked():
                self.spinBox_EllipseCenterX.clear()
                self.spinBox_EllipseCenterX.setValue(parx)
            if self.checkBox_Line.isChecked():
                self.spinBox_LineStartX.clear()
                self.spinBox_LineStartX.setValue(parx)
                
        if self.par_2.isChecked():
            if self.checkBox_Rectangle.isChecked():
                self.spinBox_RectangleLeftUpY.clear()
                self.spinBox_RectangleLeftUpY.setValue(pary)
            if self.checkBox_Circle.isChecked():
                self.spinBox_CircleCenterY.clear()
                self.spinBox_CircleCenterY.setValue(pary)
            if self.checkBox_Ellipse.isChecked():
                self.spinBox_EllipseCenterY.clear()
                self.spinBox_EllipseCenterY.setValue(pary)
            if self.checkBox_Line.isChecked():
                self.spinBox_LineStartY.clear()
                self.spinBox_LineStartY.setValue(pary)
                
        if self.par_3.isChecked():
            if self.checkBox_Rectangle.isChecked():
                self.spinBox_RectangleWidth.clear()
                self.spinBox_RectangleWidth.setValue(parx-self.spinBox_RectangleLeftUpX.value())
            if self.checkBox_Circle.isChecked():
                self.spinBox_CircleRadius.clear()
                self.spinBox_CircleRadius.setValue( sqrt((self.spinBox_CircleCenterX.value()-parx)**2 + (self.spinBox_CircleCenterY.value()-pary)**2))
            if self.checkBox_Ellipse.isChecked():
                self.spinBox_EllipseRadiiX.clear()
                self.spinBox_EllipseRadiiX.setValue(parx-self.spinBox_EllipseCenterX.value())
            if self.checkBox_Line.isChecked():
                self.spinBox_LineEndX.clear()
                self.spinBox_LineEndX.setValue(parx)
                
        if self.par_4.isChecked():
            if self.checkBox_Rectangle.isChecked():
                self.spinBox_RectangleHeight.clear()
                self.spinBox_RectangleHeight.setValue(pary-self.spinBox_RectangleLeftUpY.value())
            if self.checkBox_Ellipse.isChecked():
                self.spinBox_EllipseRadiiY.clear()
                self.spinBox_EllipseRadiiY.setValue(pary-self.spinBox_EllipseCenterY.value())
            if self.checkBox_Line.isChecked():
                self.spinBox_LineEndY.clear()
                self.spinBox_LineEndY.setValue(pary)
                
        
    def click(self):
        print("tangohost")
        self.label.setText(os.environ[ "TANGO_HOST" ])
        self.label_2.setText("Available devices:")
        db = PyTango.Database()
        list=db.get_device_alias_list("*")
        self.comboBox_UnassignedDevices.addItems(list)
        
    def wheelEventEncountered(self, wheel_integer):
        print("Got %d from signal" % wheel_integer)
        if wheel_integer>0:
            self.wheel_integer_count+=1
        else:
            self.wheel_integer_count-=1
        
        path = str(self.lineEdit_PictureName.text())+".svg"
        if os.path.isfile(path):
            path = path[:-4]
            if self.wheel_integer_count == 0:
                self.scene.clear()
                self.scene.addPixmap(QtGui.QPixmap(path+".svg").scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio))
                
            elif self.wheel_integer_count == 1:  #and wheel_integer > 0
                path = path + ".svg"
                if not os.path.isfile(path):
                    addlayer.addlayer(path, str(self.lineEdit_PictureName.text()))
                path = path[:-4]
                self.scene.clear()
                self.scene.addPixmap(QtGui.QPixmap(path+"v2.svg").scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio))
            elif self.wheel_integer_count == 2:  #and wheel_integer > 0
                path = path + "v2.svg"
                if not os.path.isfile(path):
                    addlayer.addlayer_2(path)
                path = path[:-6]
                self.scene.clear()
                self.scene.addPixmap(QtGui.QPixmap(path+"v3.svg").scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio))
            #elif self.wheel_integer_count == 
            #self.scene.addPixmap(QtGself.QPixmap(path))
        else:
            path = path[:-4]
            path = 'resources/' + path
            if self.wheel_integer_count == 0:
                self.scene.clear()
                self.scene.addPixmap(QtGui.QPixmap(path+".svg").scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio))
            
            elif self.wheel_integer_count == 1: #and wheel_integer > 0
#                path = path[:-4]
#                path = path + "v2.svg"
                if not os.path.isfile(path+"v2.svg"):
#                    path = path[:-6]
                    addlayer.addlayer(path+".svg", str(self.lineEdit_PictureName.text()))
                    
#                path = path[:-4]
                self.scene.clear()
                self.scene.addPixmap(QtGui.QPixmap(path+"v2.svg").scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio))
                
            elif self.wheel_integer_count == 2: #and wheel_integer > 0
#                path = path[:-6]
#                path = path + "v3.svg"
                if not os.path.isfile(path+"v3.svg"):
                    addlayer.addlayer_2(path+"v2.svg")
#                    path = path[:-6]
#                path = path[:-6]
                self.scene.clear()
                self.pixmap = QtGui.QPixmap(path+"v3.svg").scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio)
                self.scene.addPixmap(self.pixmap)
                self._height = self.graphicsView.geometry().height()
                self._width = self.graphicsView.geometry().width()
                print(type(self.graphicsView.geometry().width()))
                print(type(self._width))
                
            elif self.wheel_integer_count > 2:
                
                self._height = self._height + int(0.1*wheel_integer)
                #newHeight = self.parent.geometry().height() - event.delta()
                self._width = self._width + int(0.1*wheel_integer)
                self.scene.clear()
                #self.parent.resize(width, newHeight)
                self.scene.addPixmap(QtGui.QPixmap(path+"v3.svg").scaled(self._width, self._height, QtCore.Qt.KeepAspectRatio))

            elif self.wheel_integer_count < 0:
                self._height = self._height + int(0.1*wheel_integer)
                #newHeight = self.parent.geometry().height() - event.delta()
                self._width = self._width + int(0.1*wheel_integer)
                self.scene.clear()
                #self.parent.resize(width, newHeight)
                self.scene.addPixmap(QtGui.QPixmap(path+".svg").scaled(self._width, self._height, QtCore.Qt.KeepAspectRatio))
            

            #    path = path + "v2.svg"
            #    addlayer.addlayer_2(path)
            #self.scene.addPixmap(QtGself.QPixmap(path))
        
        #scene.addPixmap(QtGui.QPixmap(self.pictureName+"v2.svg").scaled(self.size(), QtCore.Qt.KeepAspectRatio))
        
        
        """"
            path = str(self.lineEdit_PictureName.text())+".svg"
            if os.path.isfile(path):
                
            else:
                path = path[:-4]
                path = 'resources/' + path
                #self.scene.addPixmap(QtGui.QPixmap(path))
                self.scene.clear()
                self.scene.addPixmap(QtGui.QPixmap(path+".svg").scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio))
            #self.scene.addPixmap(QtGui.QPixmap(ui.c+".svg").scaled(ui.graphicsView.size(), QtCore.Qt.KeepAspectRatio))
        """
        """
        
        path = str(self.lineEdit_PictureName.text())+".svg"
        if os.path.isfile(path):
            print path
            path = path[:-4]
            print path
            self.scene(clear)
            self.scene.addPixmap(QtGui.QPixmap(path+"v2.svg").scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio))
        else:
            path = path[:-4]
            path = 'resources/' + path
                #self.scene.addPixmap(QtGui.QPixmap(path))
            self.scene.clear()
            self.scene.addPixmap(QtGui.QPixmap(path+"v2.svg").scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio))
        """
        
        self.graphicsView.setScene(self.scene)
        
     
    
    def clicked_Refresh_button(self):  #for Refresh button
        self.scene.clear()
        
    def clicked_AssignIconToDevice_button(self):
        
        path = "devicesandicons.xml"
        if not os.path.isfile(str(path)):        
            self.xml.add(self.picturefile, self.comboBox_UnassignedDevices.currentText(), self.lineEdit_PictureWidth.text(), self.lineEdit_PictureHeight.text())
        else:
            self.xml.tree = ETree.parse('devicesandicons.xml')
            self.xml.root = self.xml.tree.getroot()
            #for rank in self.xml.root.iter('device'):
            rank = ETree.SubElement(self.xml.root, "device")
            self.xml.deviceName = ETree.SubElement(rank, "deviceName")
            self.xml.deviceName.text = str(self.comboBox_UnassignedDevices.currentText())
            self.xml.pictureFile = ETree.SubElement(rank, "pictureFile")
            self.xml.pictureFile.text = str(self.picturefile)
            self.pictureWidth = ETree.SubElement(rank, "pictureWidth")
            self.pictureWidth.text = str(self.lineEdit_PictureWidth.text())
            self.pictureHeight = ETree.SubElement(rank, "pictureHeight")
            self.pictureHeight.text = str(self.lineEdit_PictureHeight.text())            
            self.xml.tree.write('devicesandicons.xml')
        
        
        self.svg.saveDrawing()
        self.lineEdit_PictureName.clear()
        self.lineEdit_PictureWidth.clear()
        self.lineEdit_PictureHeight.clear()
        self.frame.hide()
        self.frame_2.hide()
        
    
    
        #addlayer.addlayer(self.x+".svg", self.x)

        #scaled(self.imageContainer.size(), QtCore.Qt.KeepAspectRatio)
        #b=str(self.x)+"v2"+".svg"
        #self.messageBox_ZoomOut.setIconPixmap(QPixmap(str(self.x)+"v2"+".svg").scaled(self.messageBox_ZoomOut.size(), QtCore.Qt.KeepAspectRatio))
        #self.messageBox_ZoomOut.setIconPixmap(QPixmap(str(self.x)+"v2"+".svg"))
        #self.messageBox_ZoomOut.exec_()
        
        
    
    def clicked_AssignNameAndSizesToPicture_button(self):
         self.x=self.lineEdit_PictureName.text()
         nazwa=self.x
         y=str(self.lineEdit_PictureWidth.text())
         z=str(self.lineEdit_PictureHeight.text())
         if y.isdigit():
             self.svgwidth=int(y)
         else: 
             self.svgwidth=300
         if z.isdigit():
             self.svgheight=int(z)
         else:
             self.svgheight=300
         if self.x=="":
             self.messageBox.exec_()
         else:
             self.picturefile=self.x
             self.frame.show()
             self.svg = DrawSVG(str(self.x)+".svg", self.svgwidth, self.svgheight)
             
        
    
    def choosen_UnassignedDevices_comboBox(self, Dialog):
        """
        self.grview = QGraphicsView()
        self.scene = QGraphicsScene(self.grview)
        """
        self.wheel_integer_count=0
        self.scene.clear()
        #self.graphicsView.setScene(self.scene)
        
        
        self.pushButton_AssignIconToDevice.setGeometry(QtCore.QRect(870, 380, 300, 27))
        self.frame_2.show()
        
        self.listDeviceName=[]
        self.listPictureFileName=[]
        path = "devicesandicons.xml"
        if os.path.isfile(str(path)):
            tree = ETree.parse(path)
            root = tree.getroot()
            for child in root.findall('device'):
                for child2 in child.findall('deviceName'):
                    self.listDeviceName.append(str(child2.text))
                    print(child2.text)
                for child3 in child.findall('pictureFile'):
                    self.listPictureFileName.append(str(child3.text))
                    print(child3.text)  
                    
        print(self.listDeviceName)
        print(self.listPictureFileName)
        if str(self.comboBox_UnassignedDevices.currentText()) in self.listDeviceName:
            y= self.comboBox_UnassignedDevices.currentText()
            x=self.listDeviceName.index(y)
            self.lineEdit_PictureName.insertPlainText(self.listPictureFileName[x])
            self.pushButton_AssignNameAndSizesToPicture.hide()
            self.frame.show()
            
            path = str(self.lineEdit_PictureName.text())+".svg"
            if os.path.isfile(path):
                self.scene.addPixmap(QtGui.QPixmap(path).scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio))
            else:
                path = 'resources/' + path
                self.scene.addPixmap(QtGui.QPixmap(path).scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio))
            #self.scene.addPixmap(QPixmap(str(self.lineEdit_PictureName.text())+".svg"))
            self.graphicsView.setScene(self.scene)
            #self.setScene(self.scene)
        else:
            self.lineEdit_PictureName.clear()
            self.pushButton_AssignNameAndSizesToPicture.show()
            self.lineEdit_PictureWidth.setText("300")
            self.lineEdit_PictureHeight.setText("300")
        
        #self.checkBox_Rectangle = QtGui.QcheckBox_Rectangle(Dialog)
        #self.checkBox_Rectangle.setGeometry(QtCore.QRect(100, 200, 97, 22))
        #self.checkBox_Rectangle.setObjectName(_fromUtf8("checkBox_Rectangle"))
        
    def choosen_AssignedDevices_comboBox(self, Dialog):
        
        self.wheel_integer_count=0
        
        
        #self.grview = QGraphicsView()
        #self.scene = QGraphicsScene(self.grview)
        self.scene.clear()
        #self.graphicsView.setScene(self.scene)
        
        
        
        self.pushButton_AssignIconToDevice.setGeometry(QtCore.QRect(870, 380, 300, 27))
        self.frame_2.show()
        
        self.listDeviceName=[]
        self.listPictureFileName=[]
        self.listPictureWidth=[]
        self.listPictureHeight=[]
        path = "devicesandicons.xml"
        if os.path.isfile(str(path)):
            tree = ETree.parse(path)
            root = tree.getroot()
            for child in root.findall('device'):
                for child2 in child.findall('deviceName'):
                    self.listDeviceName.append(str(child2.text))
                    print(child2.text)
                for child3 in child.findall('pictureFile'):
                    self.listPictureFileName.append(str(child3.text))
                    print(child3.text)  
                for child4 in child.findall('pictureWidth'):
                    self.listPictureWidth.append(str(child4.text))
                for child5 in child.findall('pictureHeight'):
                    self.listPictureHeight.append(str(child5.text))
         
        print(self.listDeviceName)
        print(self.listPictureFileName)
        if str(self.comboBox_AssignedDevices.currentText()) in self.listDeviceName:
            y= self.comboBox_AssignedDevices.currentText()
            x=self.listDeviceName.index(y)
            self.lineEdit_PictureName.clear()
            self.lineEdit_PictureWidth.clear()
            self.lineEdit_PictureHeight.clear()
            self.lineEdit_PictureName.setText(self.listPictureFileName[x])
            self.lineEdit_PictureWidth.setText(self.listPictureWidth[x])
            self.lineEdit_PictureHeight.setText(self.listPictureHeight[x])
            
            self.pushButton_AssignNameAndSizesToPicture.show()
            self.frame.show()
            path = str(self.lineEdit_PictureName.text())+".svg"
            if os.path.isfile(path):
                self.scene.addPixmap(QtGui.QPixmap(path).scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio))
                button_texture_1 = pyglet.image.load(path)
                button_texture_2 = pyglet.image.load('status.png')
                button_sprite_1 = pyglet.sprite.Sprite(button_texture_1, x=0, y=0)
                button_sprite_2 = pyglet.sprite.Sprite(button_texture_2, x=50, y=50)

                window = pyglet.window.Window()

            else:
                path = 'resources/' + path
                self.scene.addPixmap(QtGui.QPixmap(path))
                #.scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio)
                """
                import cairo
                import rsvg

                img =  cairo.ImageSurface(cairo.FORMAT_ARGB32, 640,480)

                ctx = cairo.Context(img)

                handler= rsvg.Handle(path)
                # or, for in memory SVG data:
                #handler= rsvg.Handle(<svg path>)
                handler.render_cairo(ctx)
                img.write_to_png("tomek.png")
                """
                
                button_texture_1 = pyglet.image.load("obraze.png")
                button_texture_2 = pyglet.image.load('status.png')
                button_sprite_1 = pyglet.sprite.Sprite(button_texture_1, x=0, y=0)
                button_sprite_2 = pyglet.sprite.Sprite(button_texture_2, x=50, y=50)

                window = pyglet.window.Window()

                @window.event
                def on_draw():
                    button_sprite_1.draw()
                    button_sprite_2.draw()
                
                @window.event
                def on_mouse_press(x, y, button, modifiers):
                    if x > button_sprite_2.x and x < (button_sprite_2.x + button_sprite_2.width):
                        if y > button_sprite_2.y and y < (button_sprite_2.y + button_sprite_2.height):
                            print("AAAAAAAAAAAAAAA")
                            try:    
                                dp = PyTango.DeviceProxy(str(self.comboBox_AssignedDevices.currentText()));
                                self.status = dp.status()
                                print(self.status)
                            except: 
                                print("Cannot connect")
                            
                            self.messageBox_status=QtGui.QMessageBox()
                            self.messageBox_status.setGeometry(QtCore.QRect(350, 350, 190, 22))
                            self.messageBox_status.setObjectName(_fromUtf8("messageBox_status"))
                            self.messageBox_status.setText("Status: "+self.status)  
                            self.messageBox_status.exec_()  
                pyglet.app.run()
            
            self.graphicsView.setScene(self.scene)
           
        else:
            self.lineEdit_PictureName.clear()
            self.pushButton_AssignNameAndSizesToPicture.show()
            self.lineEdit_PictureWidth.setText("800")
            self.lineEdit_PictureHeight.setText("600")
             
    def choosen_UnassignedDevices_comboBox_2(self):
        self.frame.hide()
        #self.frame_2.show()
        
    
    def clicked_ImportFromXML_button(self):
        
        self.listDeviceName=[]
        self.listPictureFileName=[]
        path = "devicesandicons.xml"
        if os.path.isfile(str(path)):
            tree = ETree.parse(path)
            root = tree.getroot()
            for child in root.findall('device'):
                for child2 in child.findall('deviceName'):
                    self.listDeviceName.append(child2.text)
                    print(child2.text)
                for child3 in child.findall('pictureFile'):
                    self.listPictureFileName.append(child3.text)
                    print(child3.text)
                    
        #print self.listDeviceName
        #print self.listPictureFileName
        
        #self.pushButton.hide()
        
        self.pushButton_ImportFromXML.hide()
        self.comboBox_UnassignedDevices.hide()
        self.label.hide()
        self.label_2.hide()
        self.comboBox_AssignedDevices.show()
        self.comboBox_AssignedDevices.clear()
        self.comboBox_AssignedDevices.addItems(self.listDeviceName)
    
    
    def clicked_AddPictureToNewDevice_button(self):
        try:
            db = PyTango.Database()
        except:
            print("Can's connect to database on: ", os.environ["TANGO_HOST"])
        
        class_list = db.get_class_list('*')
        list_of_all_devs = []
        
        for class_name in class_list:
            if db.get_instance_name_list(class_name):

                list_of_devs_for_class = reduce(operator.add,(list(dev for dev in db.get_device_class_list(n) \
                        if '/' in dev and not dev.startswith('dserver')) for n in \
                        ('/'.join((class_name,instance)) for instance in db.get_instance_name_list(class_name)) \

                        ))
                list_of_all_devs.append(list_of_devs_for_class)
        
        list2 = []
        for item in list_of_all_devs:
            for dev in item:
                if dev not in self.listDeviceName:
                    list2.append(dev)
        self.comboBox_UnassignedDevices.addItems(list2)
        
        self.frame.hide()
        self.frame_2.hide()
        self.pushButton_ImportFromXML.show()
        self.comboBox_AssignedDevices.hide()
        self.comboBox_UnassignedDevices.show()  
    
    
    
    
        
    def clickedradioButton_DrawRGB(self):
        if self.radioButton_DrawRGB.isChecked():
            self.frame_3.show()
            self.frame_4.hide()
        else:
             self.frame_3.hide()
             self.frame_4.show()
    
    def clickedradioButton_add(self):
        print("ooo")

        self.par_1.show()
        self.par_2.show()
        self.par_3.show()
        self.par_4.show()
      
            
    def clicked_Draw_button(self):
        #self.svg = DrawSVG('tomek.svg', 250, 250)
        #self.svg = DrawSVG("tomek.svg", self.svgwidth, self.svgheight)
        #self.scene.addPixmap(QPixmap(str("tomek.svg")))
        #self.graphicsView.setScene(self.scene)
        #square = dwg.add(dwg.rect(20,20),(80,80), fill='blue'))
        #dwg.save()
        
        if self.checkBox_Rectangle.isChecked():
            print('checked')
            x=self.spinBox_RectangleLeftUpX.value()
            y=self.spinBox_RectangleLeftUpY.value()
            z=self.spinBox_RectangleWidth.value()
            a=self.spinBox_RectangleHeight.value()
            
            
            #print self.fillcolor
            print(x, y, z, a)
            
            if not self.radioButton_DrawRGB. isChecked():
                fillcolor=self.comboBox_UnassignedDevices_PicturFillColors.currentText()
                linecolor=self.comboBox_PictureBorderColor.currentText()
                self.svg.drawRect(x, y, z, a, fillcolor, linecolor)
            else:
                rfill=self.spinBox_PictureFillColorRed.value()
                gfill=self.spinBox_PictureFillColorGreen.value()
                bfill=self.spinBox_PictureFillColorBlue.value()
                
                rline=self.spinBox_PictureBorderColorRed.value()
                gline=self.spinBox_PictureBorderColorGreen.value()
                bline=self.spinBox_PictureBorderColorBlue.value()
                
                self.svg.drawRectrgb(x, y, z, a, rfill, gfill, bfill, rline, gline, bline)
                #print "rgb values:", rfill, gfill, bfill
            #svg.saveDrawing()
            
        if self.checkBox_Circle.isChecked():
            print('checked2')
            x=self.spinBox_CircleCenterX.value()
            y=self.spinBox_CircleCenterY.value()
            z=self.spinBox_CircleRadius.value()
            if not self.radioButton_DrawRGB. isChecked():
                fillcolor=self.comboBox_UnassignedDevices_PicturFillColors.currentText()
                linecolor=self.comboBox_PictureBorderColor.currentText()
                print(x, y, z) 
                self.svg.drawCircle(x, y, z, fillcolor, linecolor)
            else:
                rfill=self.spinBox_PictureFillColorRed.value()
                gfill=self.spinBox_PictureFillColorGreen.value()
                bfill=self.spinBox_PictureFillColorBlue.value()
                
                rline=self.spinBox_PictureBorderColorRed.value()
                gline=self.spinBox_PictureBorderColorGreen.value()
                bline=self.spinBox_PictureBorderColorBlue.value()
                
                self.svg.drawCirclergb(x, y, z, rfill, gfill, bfill, rline, gline, bline)
                
            #svg.saveDrawing()
            
        if self.checkBox_Ellipse.isChecked():
            x=self.spinBox_EllipseCenterX.value()
            y=self.spinBox_EllipseCenterY.value()
            z=self.spinBox_EllipseRadiiX.value()
            a=self.spinBox_EllipseRadiiY.value()
            if not self.radioButton_DrawRGB. isChecked():
                fillcolor=self.comboBox_UnassignedDevices_PicturFillColors.currentText()
                linecolor=self.comboBox_PictureBorderColor.currentText()
                print(x, y, z, a)
                self.svg.drawEllipse(x, y, z, a, fillcolor, linecolor)
                print("narysowalem elopse")
            else:
                rfill=self.spinBox_PictureFillColorRed.value()
                gfill=self.spinBox_PictureFillColorGreen.value()
                bfill=self.spinBox_PictureFillColorBlue.value()
                
                rline=self.spinBox_PictureBorderColorRed.value()
                gline=self.spinBox_PictureBorderColorGreen.value()
                bline=self.spinBox_PictureBorderColorBlue.value()
                
                self.svg.drawEllipsergb(x, y, z, a, rfill, gfill, bfill, rline, gline, bline)
            #svg.saveDrawing()
            
        if self.checkBox_Line.isChecked():
            x=self.spinBox_LineStartX.value()
            y=self.spinBox_LineStartY.value()
            z=self.spinBox_LineEndX.value()
            a=self.spinBox_LineEndY.value()
            
            if not self.radioButton_DrawRGB. isChecked():
                linecolor=self.comboBox_PictureBorderColor.currentText()
                print(x, y, z, a)
                self.svg.drawLine(x, y, z, a, linecolor)
            else:
              
                rline=self.spinBox_PictureBorderColorRed.value()
                gline=self.spinBox_PictureBorderColorGreen.value()
                bline=self.spinBox_PictureBorderColorBlue.value()
                
                self.svg.drawLinergb(x, y, z, a, rline, gline, bline)
            #svg.saveDrawing()
        self.svg.saveDrawing() 
        #scene = QGraphicsScene()
        #global scene
        
      
        #self.scene.addPixmap(QPixmap(str(self.lineEdit_PictureName.text())+".svg"))
        path = str(self.lineEdit_PictureName.text())+".svg"
        if os.path.isfile(path):
            self.scene.addPixmap(QtGui.QPixmap(path).scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio))
        else:
            path = 'resources/' + path
            self.scene.addPixmap(QtGui.QPixmap(path).scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio))
        
        
        
        #self.scene.addPixmap(QPixmap(str("tomek.svg")))
        self.graphicsView.setScene(self.scene)
        
        
        
        #self.svg.showDrawing()
    
        
        
        
    
  
        
        
        

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Widget", None))
        
        #self.pushButton.setText(_translate("Dialog", "select Tango_Host", None))
        
        self.checkBox_Rectangle.setText(_translate("Dialog", "Rectangle", None))
        self.checkBox_Circle.setText(_translate("Dialog", "Circle", None))
        self.checkBox_Ellipse.setText(_translate("Dialog", "Ellipse", None))
        self.checkBox_Line.setText(_translate("Dialog", "Line", None))
        self.pushButton_Refresh.setText(_translate("Dialog", "Refresh", None))
        self.radioButton_DrawRGB.setText(_translate("Dialog", "Switch RGB selecting", None))
        self.radioButton_add.setText(_translate("Dialog", "Switch getting parameters from graphicsView", None))
        self.pushButton_AssignIconToDevice.setText(_translate("Dialog", "Assign the picture to the device", None))
        self.pushButton_AssignNameAndSizesToPicture.setText(_translate("Dialog", "Assign the name and sizes", None))
        self.pushButton_ImportFromXML.setText(_translate("Dialog", "Import data from XML", None))
        self.pushButton_Draw.setText(_translate("Dialog", "Draw", None))
        self.pushButton_AddPictureToNewDevice.setText(_translate("Dialog", "Add picture to new device", None))
        self.pushButton_8.setText(_translate("Dialog", "Show picture", None))
        
        
    
"""
class Scroll(QScrollArea):
    
    def __init__(self, parent=None):
        super(Scroll, self).__init__(parent)
        self.parent = parent
    
    def wheelEvent(self, event):
        super(Scroll, self).wheelEvent(event)
        print "wheelEvent", event.delta()

        #Ui_Widget.self.scene.clear()
        #addlayer.addlayer(self.pictureName+".svg", self.pictureName)
        #Ui_Widget.scene.addPixmap(QtGui.QPixmap(self.pictureName+"v2.svg").scaled(self.size(), QtCore.Qt.KeepAspectRatio))
        newHeight = self.parent.geometry().height() - event.delta()
        width     = self.parent.geometry().width() - event.delta()
        self.parent.resize(width, newHeight)
    
        
    def setScene(self, scene):
        self.scene=scene
        self.setScene(self.scene)
    """


        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Widget = QtGui.QWidget()
    ui = Ui_Widget()
    #ui = Scroll()
    ui.setupUi(Widget)
    Widget.show()
  
    sys.exit(app.exec_())
    
    

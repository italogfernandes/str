# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# FEDERAL UNIVERSITY OF UBERLANDIA
# Faculty of Electrical Engineering
# Biomedical Engineering Lab
# ------------------------------------------------------------------------------
# Author: Italo Gustavo Sampaio Fernandes
# Contact: italogsfernandes@gmail.com
# Git: www.github.com/italogfernandes
# ------------------------------------------------------------------------------
# Decription:
# ------------------------------------------------------------------------------
from ThreadHandler import InfiniteTimer
from Queue import Queue

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
from PyQt4.QtGui import QBrush, QColor, QPen, QGraphicsRectItem
# ------------------------------------------------------------------------------


class pyqtgraphHandler:
    def __init__(self, qnt_pontos=10):
        self.qnt_pontos = qnt_pontos

        self.app = QtGui.QApplication([])
        self.plot = pg.plot()

        self.plot.setBackgroundBrush(QBrush(QColor.fromRgb(255, 255, 255)))
        #self.plot.windowTitle().
        #self.plot.setForegroundBrush(QBrush(QColor.fromRgb(250,0,0,30)))
        self.plot.setWindowTitle('PlotterHandler')
        self.plot.setRange(QtCore.QRectF(0, -10, 5000, 20))
        self.plot.setLabel('bottom', 'Index', units='un')
        self.plot.setLabel('left', 'Valor', units='V')
        self.curve = self.plot.plot(pen='b')
        # self.plot.enableAutoRange('xy', True)
        self.plot.enableAutoRange('xy', False)
        self.plot.setXRange(0, 5000)
        self.plot.setYRange(0, 5)

        #self.plot.enableAutoRange('xy', True)
        #grade = pg.GridItem()
        #self.plot.addItem(grade)
        self.plot.showGrid(True, True)
        #self.plot.showAxis('top', False)
        #self.plot.showAxis('bottom', False)
        #self.plot.showAxis('left', False)
        #self.plot.showAxis('right', False)
        self.plot.getAxis('left').setPen(QPen(QColor.fromRgb(0,0,0)))
        self.plot.getAxis('bottom').setPen(QPen(QColor.fromRgb(0, 0, 0)))
        #print self.plot.getRange
        #self.plot.
        # self.plot.showGrid(2,3)
        #self.plot.hideAxis(ax)
        #

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_y_points)

        self.lastTime = time()
        self.fps = None

        self.y_values = [0] * self.qnt_pontos
        self.plot_buffer = Queue(qnt_pontos)


    def put(self, item):
        self.plot_buffer.put(item)

    def update_y_points(self):
        points_to_add = self.plot_buffer.qsize()
        if points_to_add > 0:
            for n in range(points_to_add): # obtains the new values
                num = self.plot_buffer.get()
                self.y_values.append(num)
                if len(self.y_values) > self.qnt_pontos:
                    self.y_values.pop(0)
            self.update()

    def update(self):
        # global curve, data, ptr, p, lastTime, fps
        self.curve.setData(self.y_values)

        now = time()
        dt = now - self.lastTime
        self.lastTime = now
        if self.fps is None:
            self.fps = 1.0 / dt
        else:
            s = np.clip(dt * 3., 0, 1)
            self.fps = self.fps * (1 - s) + (1.0 / dt) * s
        self.plot.setTitle('<font color="red">%0.2f fps</font>' % self.fps)
        self.app.processEvents()  # force complete redraw for every plot

    def get_buffers_status(self):
        return "Plot: %4d" % (self.plot_buffer.qsize()) + '/' + str(self.plot_buffer.maxsize)

    def appear(self):
        self.timer.start(0)
        import sys
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

        self.timer.stop()

if __name__ == '__main__':

    my_plot = pyqtgraphHandler(5000)

    from datetime import datetime

    def generate_point():
        agr = datetime.now()
        y_value = agr.microsecond / 1000000.0
        my_plot.put(np.sin(2*np.pi*y_value))
        #print y_value

    timer = InfiniteTimer(0.001, generate_point)
    timer.start()
    my_plot.appear()

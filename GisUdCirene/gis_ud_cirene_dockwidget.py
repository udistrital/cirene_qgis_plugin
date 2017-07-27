# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GisUdCireneDockWidget
                                 A QGIS plugin
 This plugin is for create features to GIS
                             -------------------
        begin                : 2017-07-25
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Jorge Ulises Useche Cuellar
        email                : juusechec@correo.udistrital.edu.co
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from PyQt4.QtCore import pyqtSignal

# Import by me
from qgis.core import QgsDataSourceURI, QgsVectorLayer, QgsMapLayerRegistry

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'gis_ud_cirene_dockwidget_base.ui'))


class GisUdCireneDockWidget(QtGui.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None, iface=None):
        """Constructor."""
        super(GisUdCireneDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.iface = iface
        self.loadEvents()

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

    def loadEvents(self):
        self.pushButton.clicked.connect(self.onClickedPushButton)

    def onClickedPushButton(self):
        self.loadLayer()

    def loadLayer(self):
        """DESK"""
        uri = QgsDataSourceURI()
        # set host name, port, database name, username and password
        uri.setConnection("hostname", "5432", "database", "username", "password")
        # set database schema, table name, geometry column and optionally
        # subset (WHERE clause)
        # uri.setDataSource("area_catastral", "scat", "geom", "gid > 1")
        uri.setDataSource("public", "espacio_fisico", "geometria")

        layer = QgsVectorLayer(uri.uri(False), u"Espacios Físicos", "postgres")
        if not layer.isValid():
            print "Layer failed to load!"
        else:
            print "Layer loaded!"

        QgsMapLayerRegistry.instance().addMapLayers([layer])
        # self.iface.mapCanvas().refresh()
        #
        # # https://gis.stackexchange.com/questions/131287/how-to-add-2-layers-in-qgis-and-display-them-at-the-same-time
        # canvas = self.iface.mapCanvas()
        # extent = layer.extent()
        # canvas.setExtent(extent)

        #self.iface.addVectorLayer(layer.id())
        #self.iface.mapCanvas().zoomIn()

        #vLayer = iface.activeLayer()
        # canvas = self.iface.mapCanvas()
        # extent = layer.extent()
        # canvas.setExtent(extent)
        #render = QgsMapRenderer()
        #print render.layerSet()
        #lst = [layer.id()]  # add ID of every layer
        #render.setLayerSet(lst)
        #print "Layer: "
        #print render.layerSet()

        #print self.iface
        #help(self.iface)

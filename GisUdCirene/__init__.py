# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GisUdCirene
                                 A QGIS plugin
 This plugin is for create features to GIS
                             -------------------
        begin                : 2017-07-25
        copyright            : (C) 2017 by Jorge Ulises Useche Cuellar
        email                : juusechec@correo.udistrital.edu.co
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GisUdCirene class from file GisUdCirene.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .gis_ud_cirene import GisUdCirene
    return GisUdCirene(iface)

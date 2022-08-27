#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import arcpy


"""
This file contains the settings for the automapic module.
"""


__author__ = 'Jorge Luis yupanqui Herrera'
__copyright__ = 'INGEMMET 2021'
__credits__ = ['Jorge Yupanqui H.', 'Julio Cruz F']
__version__ = '1.0.0'
__maintainer__ = 'Jorge Yupanqui H.'
__mail__ = 'jorgeluisyh@gmail.com'
__title__ = 'CatastroFiscal'
# __status__ = 'Development'
__status__ = 'Production'


_SCRIPTS_DIR = os.path.dirname(__file__)
_TEMP_FOLDER = arcpy.env.scratchFolder
_TEMP_GDB = arcpy.env.scratchGDB


_REQUIREMENTS_DIR = os.path.join(_SCRIPTS_DIR, 'require')

import arcpy
import pythonaddins
import os
import sys


BASE_DIR = os.path.dirname(__file__)
SCRIPTS_DIR = os.path.join(BASE_DIR, 'scripts')
sys.path.insert(0,SCRIPTS_DIR)

import settings_cf as st
tbx_principal = os.path.join(st._SCRIPTS_DIR, 'tbx_CatastroFiscal.tbx')

class CargarCapasClass(object):
    """Implementation for CatastroFiscalAddin_addin.btnCargarCapas (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class DuplicadoEspacialClass(object):
    """Implementation for CatastroFiscalAddin_addin.btnDuplicadoEspacial (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class DuplicadoTabularClass(object):
    """Implementation for CatastroFiscalAddin_addin.btnDuplicadoTabular (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(tbx_principal,'DuplicadoTabular')
        

class GenerarCPUClass(object):
    """Implementation for CatastroFiscalAddin_addin.btnGenerarCPU (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class GenerarIDClass(object):
    """Implementation for CatastroFiscalAddin_addin.btnGenerarID (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass

class VerificacionDominiosClass(object):
    """Implementation for CatastroFiscalAddin_addin.btnVerificacionDominios (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pass
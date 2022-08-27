#!/usr/bin/env python
# -*- coding: utf-8 -*-

import arcpy
import os
import pandas as pd
import settings_cf as st
import uuid
import pythonaddins

arcpy.env.overwriteOutput = True
sufix = uuid.uuid4().hex

def calculo_total(capas):
    """
    realiza el calculo de duplicados para todas las tablas y exporta un reporte en excel
    """
    arreglo_general = []
    arcpy.AddMessage("Validando duplicidad de registros para: ")
    for capa in capas.split(';'):
        arreglo = calcular_duplicado_tabular(capa)
        if arreglo !=0:
            arreglo_general.append(arreglo)
        
    df = pd.DataFrame(arreglo_general, dtype=str)
    df.columns = ["NombreCapa", "NumeroDuplicados","OidsAgrupados"]
    path_excel = os.path.join(st._TEMP_FOLDER,'DuplicidadTabular_{}.xls'.format(sufix))
    df.to_excel(path_excel, index=False)
    os.startfile(path_excel)

            


def calcular_duplicado_tabular(capa):
    """
    verifica si existe duplicado tabular
    """

    output_table = os.path.join(st._TEMP_GDB,'duptabular_{}'.format(sufix))
    desc = arcpy.Describe(capa)
    nombrecapa = desc.baseName
    oidField = desc.OIDFieldName
    campos =[x.name for x in desc.fields if (not x.name.startswith('Shape') and x.name!= desc.OIDFieldName)]
    arcpy.FindIdentical_management(capa, output_table, ';'.join(campos), '#', '0', 'ONLY_DUPLICATES')
    numreg = int(arcpy.GetCount_management(output_table).getOutput(0))

    arreglo =0
    if numreg > 0:
        arcpy.AddError('\t {}: {}'.format(nombrecapa,str(numreg)))
        oidlist = get_list_oids(output_table)
        arreglo =(nombrecapa, numreg, str(oidlist))
        return arreglo

    arcpy.AddMessage('\t {}: {}'.format(nombrecapa,str(numreg)))    
    return arreglo


def get_list_oids(tabla):
    """
    Obtiene el listado de oids agrupados
    """
    lista_oids=[]
    with arcpy.da.SearchCursor(tabla,["IN_FID","FEAT_SEQ"]) as cursor:
        grupo = []
        lastgroupid =0
        for row in cursor:
            if row[1]!=lastgroupid :
                if len(grupo)>0:
                    lista_oids.append(grupo)
                grupo=[]
                grupo.append(row[0])
            else:
                grupo.append(row[0])
            lastgroupid = row[1]
    
    return lista_oids

if __name__ == '__main__':
    capas = arcpy.GetParameterAsText(0)
    calculo_total(capas)
<div style="text-align:center;">
    <!-- <img src="http://www.ingemmet.gob.pe/image/layout_set_logo?img_id=73207&t=1550028890729"> -->
    <img src ="https://www.bancomundial.org/content/dam/wbr/logo/logo-wb-header-es.svg">
</div>

# Catastro Fiscal

## Qué es la herramienta de Catastro Fiscal
Ver [repositorio](https://github.com/jorgeluisyh/CatastroFiscal)

> CatastroFiscal es un esriaddin desarrollado en [Python 2.7](https://www.python.org/) para [ArcMap 10.X](http://desktop.arcgis.com/es/arcmap/10.3/main/map/what-is-arcmap-.htm), el cual brinda ayuda para realizar las taras de validación y carga de datos de municipalidades.

## Estructura

- README.md : Este archivo

- makeaddin.py : Un script que creará un archivo *.esriaddin a partir de este Proyecto, adecuado para compartir o desplegar.

- config.xml : El archivo de configuración del AddIn

- Images/* : Todas las imágenes de la interfaz de usuario para el proyecto (íconos, imágenes para botones, etc)

- Install/* : El proyecto de Python utilizado para la implementación del complemento. La secuencia de comandos de Python específica que se usará como módulo raíz, se especifica en config.xml.



## Instalación
1. Clone el repositorio remoto a un repositorio local con el comando siguiente
        
        git clone https://github.com/jorgeluisyh/CatastroFiscal.git


2. Ejecute el archivo makeaddin.py para generar el archivo *.esriaddin (tenga en cuenta realizar la edición corerspondiente para apuntar la salida del archivo a un directorio conocido de su equipo).

3. Agregar la ruta del directorio donde se aloja el archivo *.esriaddin desde ArcMap > Customize > Add-in Manager > Options > Add Folder.

## Uso
1. Se despliega automáticamente en ArcMap un toolbar que contiene las herramientas que necesitamos

## Créditos
* [JorgeLuisYH](https://github.com/jorgeluisyh)

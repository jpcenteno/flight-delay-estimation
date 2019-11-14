# TP n°3 Método Numéricos - Cuadrados Mínimos Lineales
## Intro a IA y ML.

### Inicializar submódulos

Este TP usa dos proyectos: eigen y pybind11. Para compilar es necesario descargar los submódulos e inicializarlos:

``` bash
git submodule init
git submodule update
```

Los mismos están en src/submodules

### Compilación de CML

simplemente escribir ```make``` en el directorio principal. Si el
directorio ```build``` existe, borrarlo, o escribir ```make clean```

Esto corre cmake, make y deposita el código C++ con bindings python en
la carpeta notebook listo para ser consumido.

### Descargar data

En tools hay un script download-data, se lo puedo usar de la siguiente manera:

``` bash

download-data 2008      # descarga la data del 2008
download-data carriers  # descarga los transportes
download-data airports  # descarga los aeropuertos
```

Guarda que borra todo *.bz2 en tools/ !!!

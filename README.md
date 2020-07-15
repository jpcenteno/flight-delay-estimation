# Flight Delay Estimation

This project provides an efficient C++ implementation of an Ordinary Least Squares (OLS) predictor and classifier. The OLS model was implemented using Eigen, which is a C++ library akin to Numpy. 

The OLS model was then wrapped into Python via Pybind11 to perform EDA and arrival delay prediction on a 12GB flight dataset.

This piece of code was written for the "Numerical Methods" course, taught during the second semester of 2019 at the Faculty of Natural and Exact Sciences, University of Buenos Aires.

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

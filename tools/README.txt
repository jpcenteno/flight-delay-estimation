Los datos están disponibles en http://stat-computing.org/dataexpo/2009/. 
Los mismos corresponden a información de vuelos en Estados Unidos entre
los años 1987 y 2008. Fueron parte de una competencia sobre visualización 
de datos. En la misma pagina pueden encontrarse los posters resultantes 
de la competencia, con algunas ideas respecto a visualizaciones y las 
características de los datos. 

En el sitio pueden bajar individualmente la información por año. Si 
desean bajar toda la información de una sola vez, pueden correr los
siguientes comandos:

   xargs -i wget -bqc '{}' < dataset_list.txt
   bunzip2 -k *.bz2

Notar que en el archivo `dataset_list.txt` pueden filtrar los años que
deseen descargar.

La información total comprimida ocupa cerca de 1.7 GB, y descomprimida
cerca de 12 GB. Para trabajar con los datos utilizar algunos de los
scripts que se proveen o alguna otra herramienta adecuada. 

Ejemplo: bajar los datos del año 2008 y  alojarlos en carpeta `data` 
en la misma jerarquía que las herramientas, y correr get_canc_month.sh

  mkdir data
  wget http://stat-computing.org/dataexpo/2009/2008.csv.bz2
  bunzip2 -k 2008.csv.bz2
  cd ..
  cd tools
  bash get_canc_month.sh 
  
